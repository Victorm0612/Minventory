
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    TYPE_ADMIN = 1
    TYPE_CLIENT = 2
    TYPE_EMPLOYEE = 3
    TYPE_CHOICES = ((TYPE_ADMIN, 1), (TYPE_CLIENT, 2), (TYPE_EMPLOYEE, 3))
    FEMALE = "femenino"
    MASCULINE = "masculino"
    DWTS = "prefiero_no_decirlo"
    OTHERG = "otro"
    TYPE_GENDER = ((FEMALE, "Femenino"), (MASCULINE, "Masculino"), (DWTS, "Prefiero_no_decirlo"), (OTHERG, "Otro"))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    OnlyLetters = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters.')

    username = None
    name = models.TextField(max_length=50, validators=[OnlyLetters])
    last_name = models.TextField(max_length=50, validators=[OnlyLetters])
    document_number = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.TextField(max_length=250)
    address = models.TextField(max_length=50)
    gender = models.CharField(max_length=19, choices=TYPE_GENDER)
<<<<<<< HEAD
    type = models.IntegerField(choices=TYPE_CHOICES)
=======
    type = models.TextField(max_length=8, choices=TYPE_CHOICES)
    last_login = models.DateTimeField(auto_now_add=True)
  
>>>>>>> develop
