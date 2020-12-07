from django.db import models
from api.models.statusmodels import Status
from api.models.usermodels import User
from api.models.requestquotationmodels import RequestQuotation


class Task(models.Model):
    approved_date = models.DateTimeField(auto_now_add=True)
    realization_date = models.DateTimeField()
    fkAssignment_worker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fkTask_status = models.ForeignKey(Status, related_name='Status_id', on_delete=models.CASCADE)
    fkRequestquotation = models.ForeignKey(RequestQuotation, on_delete=models.CASCADE, null=True)
