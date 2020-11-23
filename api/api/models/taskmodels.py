from django.db import models
from api.models.elementmodels import Element
from api.models.statusmodels import Status
from api.models.usermodels import User


class Task(models.Model):
    approved_date = models.DateTimeField(auto_now_add=True)
    realization_date = models.DateTimeField()
    fkAssignment_worker = models.ForeignKey(User, related_name='User_id', on_delete=models.CASCADE, null=True)
    fkElement_id = models.ForeignKey(Element, related_name='Element_id', on_delete=models.CASCADE)
    fkTask_status = models.ForeignKey(Status, related_name='Status_id', on_delete=models.CASCADE)
