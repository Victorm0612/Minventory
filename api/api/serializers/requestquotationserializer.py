from rest_framework import serializers
from api.models.requestquotationmodels import RequestQuotation


class RequestQuotationSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if data != None:
            fechaUsuario = data.get('scheduled_date')
            rangoUsuario = data.get('time_range')
            idUsuario = data.get('fkUser_id')
            ocupado = RequestQuotation.objects.filter(scheduled_date=fechaUsuario, time_range=rangoUsuario)
            modificar = RequestQuotation.objects.filter(fkUser_id=idUsuario)
            if modificar:
                return data

            elif ocupado:
                raise serializers.ValidationError({"scheduled_date_and_time_range": "Ese rango de hora en esa fecha está ocupado"})

            return data

    class Meta:
        model = RequestQuotation
        fields = '__all__'


