from django.db import models


# Create your models here.
class Status(models.Model):
    CREATED = "creada"
    ASSIGN = "asignada"
    TECNIC_REVIEW = "en_revision_por_tecnico"
    CLIENT_REVIEW = "en_revision_por_cliente"
    ACCEPTED = "aceptada"
    ENDED = "terminada"
    CANCELLED = "cancelada"
    STATUS_CHOICES = ((CREATED, "Creada"), (ASSIGN, "Asignada"), (TECNIC_REVIEW, "En_revision_por_tecnico"),
                      (CLIENT_REVIEW, "En_revision_por_cliente"), (ACCEPTED, "Aceptada"), (ENDED, "Terminada"),
                      (CANCELLED, "Cancelada"))
    description = models.TextField()
    status_type = models.TextField(max_length=12,choices=STATUS_CHOICES, default="creada")