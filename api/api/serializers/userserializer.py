from django.core import exceptions

from rest_framework import serializers
from api.models.usermodels import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
