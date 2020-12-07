from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.taskmodels import Task
from api.serializers.taskserializer import TaskSerializer
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.requestquotationmodels import RequestQuotation
from api.serializers.requestquotationserializer import RequestQuotationSerializer


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
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_task(request, fk):
    try:
        task = Task.objects.filter(fkAssignment_worker=fk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = TaskSerializer(task, many=True)
        return JSONResponse(serializer.data)

def autoTask(request):
    quotation = RequestQuotation.objects.get(pk=request)
    serializer = RequestQuotationSerializer(quotation)
    task={
        "fkRequestquotation": serializer['id']
    }

    task_serializer = TaskSerializer(task)
    if task_serializer.is_valid():
        task_serializer.save()
    return JSONResponse(serializer.errors, status=404)

