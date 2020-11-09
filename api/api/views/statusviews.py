from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.statusmodels import Status
from api.serializers.statusserializer import StatusSerializer
from django.views.decorators.csrf import csrf_protect
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
def status_list(request):
    if request.method == 'GET':
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@csrf_protect
def status_detail(request, pk):
    try:
        statu = Status.objects.get(pk=pk)
    except Status.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = StatusSerializer(statu)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StatusSerializer(statu, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        statu.delete()
        return HttpResponse(status=204)