from django.db import models


# Create your models here.
class Status(models.Model):
    fkTask_id = models.IntegerField
    description = models.TextField()