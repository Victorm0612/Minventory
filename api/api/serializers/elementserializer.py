from rest_framework import serializers
from api.models.elementmodels import Element


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'
