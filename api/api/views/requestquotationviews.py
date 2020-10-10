from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models.requestquotationmodels import RequestQuotation
from api.models.rqserializer import RequestQuotationSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
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


@csrf_exempt
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
        serializer = RequestQuotationSerializer(quotation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        quotation.delete()
        return HttpResponse(status=204)