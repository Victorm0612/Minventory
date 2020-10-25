from django.db import models


# Create your models here.
class Status(models.Model):
    description = models.TextField()