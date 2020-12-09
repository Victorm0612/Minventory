from rest_framework import serializers
from django.core import exceptions
from api.models.usermodels import User
import django.contrib.auth.password_validation as validators
from api.views import userviews



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):

        user = User(**data)

        # get the password from the data
        password = data.get('password')
        logged = data.get('actual_token')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)
            print(logged)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)