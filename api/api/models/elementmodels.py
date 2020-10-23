from django.db import models
from api.models.inventorymodels import Inventory


# Create your models here.
class Element(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    reseller = models.TextField(max_length=200)
    element_stock = models.IntegerField(default=0)
    element_stock = models.IntegerField()
    fkInventory_id = models.ForeignKey(Inventory, related_name='Inventory_id', on_delete=models.CASCADE, blank=True)

