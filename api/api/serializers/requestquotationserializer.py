from rest_framework import serializers
from api.models.requestquotationmodels import RequestQuotation


class RequestQuotationSerializer(serializers.ModelSerializer):

    def validate(self, data):
        fechaUsuario = data.get('scheduled_date')
        rangoUsuario = data.get('time_range')
        ocupado = RequestQuotation.objects.filter(scheduled_date=fechaUsuario, time_range=rangoUsuario)

        if ocupado:
            raise serializers.ValidationError({"scheduled_date and time_range": "Ese rango de hora en esa fecha está ocupado"})
        return data

    class Meta:
        model = RequestQuotation
        fields = '__all__'


