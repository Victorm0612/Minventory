from rest_framework import serializers
from api.models.requestquotationmodels import RequestQuotation


class RequestQuotationSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if data != None:
            fechaUsuario = data.get('scheduled_date')
            rangoUsuario = data.get('time_range')
            ocupado = RequestQuotation.objects.filter(
                scheduled_date=fechaUsuario, time_range=rangoUsuario)
            if ocupado:
                raise serializers.ValidationError(
                    {"scheduled_date_and_time_range": "Ese rango de hora en esa fecha está ocupado"})
            return data

    class Meta:
        model = RequestQuotation
        fields = '__all__'


class RequestQuotationPutSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if data != None:
            print(data)



    # def validate(self, data):

    #     if data != None:
    #         fechaUsuario = data.get('scheduled_date')
    #         rangoUsuario = data.get('time_range')
    #         idUsuario = data.get('fkUser_id')
    #         idQuotation = data.get('pk')
    #         # print("idQuotation: ", idQuotation)
    #         valid_user = RequestQuotation.objects.filter(
    #             scheduled_date=fechaUsuario, time_range=rangoUsuario, fkUser_id=idUsuario)
    #         ocupado = RequestQuotation.objects.filter(id=idQuotation, scheduled_date=fechaUsuario, time_range=rangoUsuario)
    #         # verificarUser = ocupado.exclude(
    #         #     scheduled_date=fechaUsuario, time_range=rangoUsuario, fkUser_id=idUsuario)

    #         if valid_user:
    #             # print("verificarUser: ", verificarUser)
    #             # print("ocupado: ", ocupado)
    #             if ocupado:

    #                 raise serializers.ValidationError(
    #                     {"scheduled_date_and_time_range": "Ese rango de hora en esa fecha está ocupado"})
    #             return data

    #         elif ocupado:
    #             raise serializers.ValidationError(
    #                 {"scheduled_date_and_time_range": "Ese rango de hora en esa fecha está ocupado"})
    #         return data

    class Meta:
        model = RequestQuotation
        fields = '__all__'
