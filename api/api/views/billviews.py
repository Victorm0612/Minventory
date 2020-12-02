from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.billmodels import Bill
from api.serializers.billserializer import BillSerializer
from api.models.taskmodels import Task
from api.serializers.taskserializer import TaskSerializer
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
def bill_list(request):
    if request.method == 'GET':
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BillSerializer(data=data)
        task = data.get('fkTask')
        print(task)
        try:
            finished = Task.objects.get(pk=task, fkTask_status=6)
            if finished:
                if serializer.is_valid():
                    serializer.save()
                    return JSONResponse(serializer.data)
                return JSONResponse(serializer.errors, status=400)
        except Task.DoesNotExist:
            return JSONResponse("Esa tarea está en curso, por favor pasarla a estado Finalizado")
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def bill_detail(request, pk):
    try:
        bill = Bill.objects.get(pk=pk)
    except Bill.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = BillSerializer(bill)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BillSerializer(bill, data=data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        bill.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bill_type(request, bill_type):
    try:
        quotation = Bill.objects.filter(bill_type=bill_type)
    except Bill.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = BillSerializer(quotation, many=True)
        return JSONResponse(serializer.data)
