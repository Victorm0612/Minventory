from django.db import models


# Create your models here.

#Formato
DATE_INPUT_FORMATS = ['%d-%m-%Y']

class Bill(models.Model):
    bill_date = models.DateField()
    total_price = models.IntegerField(default=0)
    description = models.TextField()