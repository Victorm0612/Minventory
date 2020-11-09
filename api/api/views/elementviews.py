from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.elementmodels import Element
from api.serializers.elementserializer import ElementSerializer
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_protect
def element_list(request):
    if request.method == 'GET':
        elements = Element.objects.all()
        serializer = ElementSerializer(elements, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ElementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@csrf_protect
def element_detail(request, pk):
    try:
        element = Element.objects.get(pk=pk)
    except Element.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ElementSerializer(element)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ElementSerializer(element, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        element.delete()
        return HttpResponse(status=204)
