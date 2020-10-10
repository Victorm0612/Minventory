from rest_framework import serializers
from api.models.statusmodels import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
