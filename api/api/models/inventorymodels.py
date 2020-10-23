from django.db import models


class Inventory(models.Model):
    # La fecha aqui es autogenerada, en el momento en que se realice un
    # cambio respecto a un elemento relacionado con algún inventario,
    # se autogenera la fecha el dia que se cambió
    date_log = models.DateTimeField(auto_now_add=True)


