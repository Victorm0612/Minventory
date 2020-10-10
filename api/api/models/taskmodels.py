from django.db import models


# Create your models here.
class Task(models.Model):
    approved_date = models.DateTimeField()
    realization_date = models.DateTimeField()
    fkAssignment_worker = models.IntegerField(default=0)
    fkElement_id = models.IntegerField(default=0)
    fkTask_status = models.IntegerField(default=0)
