from django.db import models


# Create your models here.
class Element(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    reseller = models.TextField(max_length=200)
    element_stock = models.IntegerField(default=0)
