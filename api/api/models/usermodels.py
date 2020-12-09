from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    TYPE_ADMIN = 1
    TYPE_CLIENT = 2
    TYPE_EMPLOYEE = 3
    TYPE_CHOICES = ((TYPE_ADMIN, 1), (TYPE_CLIENT, 2), (TYPE_EMPLOYEE, 3))
    FEMALE = "femenino"
    MASCULINE = "masculino"
    DWTS = "prefiero_no_decirlo"
    OTHERG = "otro"
    CC = "cedula_de_ciudadania"	
    CE = "cedula_de_extranjeria"	
    PSPT ="pasaporte"	
    NIT ="nit"
    TYPE_GENDER = ((FEMALE, "Femenino"), (MASCULINE, "Masculino"), (DWTS, "Prefiero_no_decirlo"), (OTHERG, "Otro"))
    TYPE_DOCUMENT = ((CC,"Cedula_de_ciudadania"),(CE,"Cedula_de_extranjeria"),(PSPT,"Pasaporte"),(NIT,"NIT"))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    avatar = models.TextField(default="DEFAULT")

    OnlyLetters = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters.')

    username = None
    name = models.TextField(max_length=50, validators=[OnlyLetters])
    last_name = models.TextField(max_length=50, validators=[OnlyLetters])
    document_type = models.CharField(max_length=21, choices=TYPE_DOCUMENT)
    document_number = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.TextField(max_length=250)
    address = models.TextField(max_length=50)
    gender = models.CharField(max_length=19, choices=TYPE_GENDER)
    type = models.TextField(max_length=8, choices=TYPE_CHOICES)
    last_login = models.DateTimeField(auto_now_add=True)
    actual_token = models.TextField(null=True)
