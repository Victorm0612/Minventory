from django.db import models


# Create your models here.
class Inventory(models.Model):
    date_log = models.DateTimeField()

