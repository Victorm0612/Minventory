from django.db import models
from api.models.elementmodels import Element
from api.models.taskmodels import Task


class TaskElement(models.Model):
    fkTask_id = models.ForeignKey(Task, related_name='Task_id', on_delete=models.CASCADE)
    fkElement_id = models.ForeignKey(Element, related_name='Task_id', on_delete=models.CASCADE)