from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.elementmodels import Element
from api.serializers.elementserializer import ElementSerializer

# Trabajar a partir de aqui
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
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


@csrf_exempt
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

