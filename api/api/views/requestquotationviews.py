from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.requestquotationmodels import RequestQuotation
from api.serializers.requestquotationserializer import RequestQuotationSerializer
from api.models.taskmodels import Task
from api.serializers.taskserializer import TaskSerializer
from api.views import taskviews
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import json


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
def quotation_list(request):
    if request.method == 'GET':
        quotations = RequestQuotation.objects.all()
        serializer = RequestQuotationSerializer(quotations, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RequestQuotationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def quotation_detail(request, pk):
    try:
        quotation = RequestQuotation.objects.get(pk=pk)
    except RequestQuotation.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = RequestQuotationSerializer(quotation)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        statustype = data.get('fkTask_status')
        ocupado = RequestQuotation.objects.filter(
            scheduled_date=data['scheduled_date'], time_range=data['time_range']).exclude(pk=pk)
        if ocupado:
            return JSONResponse("Ese rango de hora en esa fecha está ocupado", status=400)
        for key, value in data.items():
            quotation.update_field(key, value)
        try:
            if statustype == 5:

                task = {
                    "approved_date": "2020-12-07 09:43:15",
                    "realization_date": "2020-11-10 12:30:00",
                    "fkAssignment_worker": 1,
                    "fkTask_status": 1,
                    "fkRequestquotation": str(pk)
                }
                task_serializer = TaskSerializer(data=task)

                if task_serializer.is_valid():
                    task_serializer.save()
            quotation.save(update_fields=data.keys())
            return JSONResponse("La cotizacion se edito con exito!", status=200)
        except Exception:
            return JSONResponse("Error actualizando la cotizacion!", status=500)

    elif request.method == 'DELETE':
        quotation.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_quotation(request, fk):
    try:
        quotation = RequestQuotation.objects.filter(fkUser_id=fk)
    except RequestQuotation.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = RequestQuotationSerializer(quotation, many=True)
        return JSONResponse(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def date_quotation(request, scheduled_date):
    try:
        quotation = RequestQuotation.objects.filter(scheduled_date=scheduled_date)
    except RequestQuotation.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = RequestQuotationSerializer(quotation, many=True)
        return JSONResponse(serializer.data)
