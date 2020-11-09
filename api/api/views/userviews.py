from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.usermodels import User
from rest_framework.response import Response
from api.serializers.userserializer import UserSerializer
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import exceptions
from api.utils.authutils import generate_access_token, generate_refresh_token


class JSONResponse(HttpResponse):

    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    User = get_user_model()
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'El email y el password son requeridos')
    user = User.objects.filter(email=email).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('Usuario no encontrado')
    if (user.password != password):
        raise exceptions.AuthenticationFailed('Email y/o password incorrectos')
    serialized_user = UserSerializer(user).data
    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)
    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }
    user.actual_token = access_token
    user.save()

    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    User = get_user_model()
    refresh_token = request.COOKIES.get('refreshtoken')
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Las credenciales de autenticacion no fueron dadas.')
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'El token expiro, por favor vuelve a iniciar sesion.')

    user = User.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('No se encontro el usuario')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('El ususario esto incativo')


    access_token = generate_access_token(user)
    user.actual_token = access_token
    user.save()

    return Response({'access_token': access_token})
