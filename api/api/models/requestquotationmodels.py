from django.db import models
from api.models.usermodels import User


# Create your models here.
class RequestQuotation(models.Model):
    # La @request_date se autogenera al momento de pedir la cita
    request_date = models.DateTimeField(auto_now_add=True)

    # la @scheduled_date es la que el cliente debe asignarle
    # Formato: YYYY-MM-DD
    scheduled_date = models.DateField()
    approved = models.BooleanField()
    service_type = models.TextField(max_length=50)
    description = models.TextField(max_length=200)
    fkUser_int = models.ForeignKey(User, related_name='User_id', on_delete=models.CASCADE)