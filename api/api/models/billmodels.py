from django.db import models

# Create your models here.


class Bill(models.Model):
    # La fecha aqui es autogenerada, al momento de crearse la factura,
    # se ingresa la fecha del dia en que se creó
    bill_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
