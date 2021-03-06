from rest_framework import serializers
from api.models.taskmodels import Task
from api.models.usermodels import User
from api.serializers.userserializer import UserSerializer


class TaskSerializer(serializers.ModelSerializer):

    def validate(self, data):
        
        if data.get('fkAssignment_worker') != None:
            try:
                idUsuario = data.get('fkAssignment_worker')
                user = User.objects.get(email=idUsuario)
            except User.DoesNotExist:
                raise serializers.ValidationError({"user_email": "El usuario no se encuentra en el sistema"})

            serializer = UserSerializer(user)
            datos = serializer.data

            tipoUsuario = datos.get('type')

            if tipoUsuario != 3:
                raise serializers.ValidationError({"user_type": "El usuario no es empleado"})

            return data
        return data

    class Meta:
        model = Task
        fields = '__all__'
