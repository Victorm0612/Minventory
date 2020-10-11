from rest_framework import serializers
from django.core import exceptions
from api.models.usermodels import User
import django.contrib.auth.password_validation as validators



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'name','last_name','document_number','phone','email','password','address','gender','type'

    def validate(self, data):

        user = User(**data)

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)