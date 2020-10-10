from django.db import models


# Create your models here.
class RequestQuotation(models.Model):
    request_date = models.DateTimeField()
    scheduled_date = models.DateTimeField()
    approved = models.BooleanField()
    service_type = models.TextField(max_length=50)
    description = models.TextField(max_length=200)
    fkUser_int = models.IntegerField()