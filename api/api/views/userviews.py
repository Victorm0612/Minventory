import jwt
from django.conf import settings
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
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

savetype = 0

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
        usertype = data.get('type')
        serializer = UserSerializer(data=data)

        if serializer.is_valid() and usertype != 3:
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
    useri = User.objects.filter(email=email).first()
    type_user = UserSerializer(useri).data
    global savetype
    savetype = type_user.get('type')

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

def print_type():
    print(savetype)
    if savetype == 3:
        print("hola")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def refresh_token_view(request):
    User = get_user_model()
    user_id = request.data.get('id')
    user = User.objects.get(pk=user_id)
    if user is None:
        raise exceptions.AuthenticationFailed('No se encontro el usuario')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('El ususario esta inactivo')

    if user.actual_token == '':
        raise exceptions.AuthenticationFailed('El token no es valido, usuario no logueado')

    access_token = generate_access_token(user)
    user.actual_token = access_token
    user.save()

    return Response({'access_token': access_token})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    User = get_user_model()
    user_id = request.data.get('id')
    response = Response()
    user = User.objects.get(pk=user_id)
    if(user is None):
        raise exceptions.AuthenticationFailed('Usuario no encontrado')
    user.actual_token = ''
    user.save()

    return Response({'Status':'Sesion cerrada con exito.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users_by_type(request, type):
    try:
        users = User.objects.filter(type=type)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        userType = data.get('type')
        serializer = UserSerializer(data=data)
        is_adm = savetype

        if serializer.is_valid() and userType == 3 and is_adm == 1:
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse({"Creating_employee": "Usted no es un usuario admin, "
                                              "no puede crear un empleado"},status=400)