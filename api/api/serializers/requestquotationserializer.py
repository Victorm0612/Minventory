from rest_framework import serializers
from api.models.requestquotationmodels import RequestQuotation


class RequestQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestQuotation
        fields = '__all__'
