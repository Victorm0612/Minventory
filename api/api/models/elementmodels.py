from django.db import models
from api.models.inventorymodels import Inventory


class Element(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200, blank=True)
    price = models.IntegerField()
    reseller = models.TextField(max_length=200)
    element_stock = models.IntegerField()
    fkInventory_id = models.ForeignKey(Inventory, related_name='Inventory_id', on_delete=models.CASCADE, default=0)

