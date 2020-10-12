from rest_framework import serializers
from api.models.inventorymodels import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
