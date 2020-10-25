from django.db import models


# Create your models here.
class Task(models.Model):
    # Al momento de crearse una tarea, quiere decir que fue aprobada
    # por ende, la fecha de aprobacion es el dia en que se crea
    # y en consecuencia, se crea automaticamente
    approved_date = models.DateTimeField(auto_now_add=True)

    # La @realization_date tiene que ser asignada por el admin, es la
    # fecha en que se realiza el trabajo, por tanto no es autoasignada
    realization_date = models.DateTimeField()
    fkAssignment_worker = models.IntegerField()
    fkElement_id = models.IntegerField()
    fkTask_status = models.IntegerField()
