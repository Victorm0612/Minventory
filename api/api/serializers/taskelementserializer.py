from rest_framework import serializers
from api.models.taskelementmodels import TaskElement


class TaskElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskElement
        fields = '__all__'