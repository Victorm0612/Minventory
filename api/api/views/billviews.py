from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.billmodels import Bill
from api.serializers.billserializer import BillSerializer
from api.models.taskmodels import Task
from api.serializers.taskserializer import TaskSerializer
from api.models.requestquotationmodels import RequestQuotation
from api.serializers.requestquotationserializer import RequestQuotationSerializer
from api.models.usermodels import User
from api.serializers.userserializer import UserSerializer
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
        type = data.get('bill_type')

        if type == "ingreso":
            try:
                finished = Task.objects.get(pk=task, fkTask_status=6)
                if finished:
                    if serializer.is_valid():
                        serializer.save()
                        return JSONResponse(serializer.data)
                    return JSONResponse(serializer.errors, status=400)
            except Task.DoesNotExist:
                return JSONResponse("Esa tarea está en curso, por favor pasarla a estado Finalizado", status=400)
        elif type == "egreso":
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
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

        if serializer.data['bill_type'] == "ingreso":
            task = Task.objects.get(pk=serializer.data['fkTask'])
            task_serializer = TaskSerializer(task)
            request_quotation = RequestQuotation.objects.get(pk=task_serializer.data['fkRequestquotation'])
            quotation_serializer = RequestQuotationSerializer(request_quotation)
            user = User.objects.get(pk=quotation_serializer.data['fkUser_id'])
            user_serializer = UserSerializer(user)

            taskBill_list = {
                "id": serializer.data['id'],
                "bill_date": serializer.data['bill_date'],
                "bill_type": serializer.data['bill_type'],
                "total_price": serializer.data['total_price'],
                "description": serializer.data['description'],
                "task_id": serializer.data['fkTask'],
                "approved_date": task_serializer.data['approved_date'],
                "realization_date": task_serializer.data['realization_date'],
                "fkAssignment_worker": task_serializer.data['fkAssignment_worker'],
                "fkTask_status": task_serializer.data['fkTask_status'],
                "user_id": user_serializer.data['id'],
                "name": user_serializer.data['name'],
                "last_name": user_serializer.data['last_name'],
                "document_type": user_serializer.data['document_type'],
                "document_number": user_serializer.data['document_number'],
                "phone": user_serializer.data['phone'],
                "email": user_serializer.data['email'],
            }
            return JSONResponse(taskBill_list)

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
        bills = Bill.objects.filter(bill_type=bill_type)
    except Bill.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and bill_type == "egreso":
        serializer = BillSerializer(bills, many=True)
        return JSONResponse(serializer.data)

    if request.method == 'GET' and bill_type == "ingreso":
        serializer = BillSerializer(bills, many=True)

        egress_list = []

        for i in range(0, bills.count()):
            bill_index = serializer.data[i]
            task = Task.objects.get(pk=bill_index['fkTask'])
            task_serializer = TaskSerializer(task)
            request_quotation = RequestQuotation.objects.get(pk=task_serializer.data['fkRequestquotation'])
            quotation_serializer = RequestQuotationSerializer(request_quotation)
            user = User.objects.get(pk=quotation_serializer.data['fkUser_id'])
            user_serializer = UserSerializer(user)

            taskBill_list = {
                "id": bill_index['id'],
                "bill_date": bill_index['bill_date'],
                "bill_type": bill_index['bill_type'],
                "total_price": bill_index['total_price'],
                "description": bill_index['description'],
                "task_id": bill_index['fkTask'],
                "approved_date": task_serializer.data['approved_date'],
                "realization_date": task_serializer.data['realization_date'],
                "assignment_worker_id": task_serializer.data['fkAssignment_worker'],
                "task_status_id": task_serializer.data['fkTask_status'],
                "user_id": user_serializer.data['id'],
                "name": user_serializer.data['name'],
                "last_name": user_serializer.data['last_name'],
                "document_type": user_serializer.data['document_type'],
                "document_number": user_serializer.data['document_number'],
                "phone": user_serializer.data['phone'],
                "email": user_serializer.data['email'],
            }
            egress_list.append(taskBill_list)


        return JSONResponse(egress_list)
