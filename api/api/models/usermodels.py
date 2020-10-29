
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    
    TYPE_ADMIN = "admin"
    TYPE_CLIENT = "client"
    TYPE_EMPLOYEE = "employee"
    TYPE_CHOICES = ((TYPE_ADMIN, 1), (TYPE_CLIENT, 2), (TYPE_EMPLOYEE, 3))
    FEMALE = "femenino"
    MASCULINE = "masculino"
    DWTS = "prefiero_no_decirlo"
    OTHERG = "otro"
    TYPE_GENDER = ((FEMALE, "Femenino"), (MASCULINE, "Masculino"), (DWTS, "Prefiero_no_decirlo"), (OTHERG, "Otro"))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Validar que solo se ingresen letras y espacios en el campo
    OnlyLetters = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters.')

    username = None
    name = models.TextField(max_length=50, validators=[OnlyLetters])
    last_name = models.TextField(max_length=50, validators=[OnlyLetters])
    document_number = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True)
    # EmailField=verifica que tenga @ y unique para que no esté usado
    email = models.EmailField(max_length=200,unique=True)
    password = models.TextField(max_length=250)
    address = models.TextField(max_length=50)
    gender = models.CharField(max_length=19, choices=TYPE_GENDER)
    type = models.TextField(max_length=8, choices=TYPE_CHOICES)
    last_login = models.DateTimeField(auto_now_add=True)
  
