from django.db import models
from api.models.taskmodels import Task


class Bill(models.Model):
    EGRESS = "egreso"
    INGRESS = "ingreso"
    TYPE_BILL = ((EGRESS, "Egreso"), (INGRESS, "Ingreso"))

    bill_date = models.DateTimeField(auto_now_add=True)
    bill_type = models.TextField(max_length=7, choices=TYPE_BILL)
    total_price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    fkTask = models.ForeignKey(Task, related_name='Task_id', on_delete=models.CASCADE)