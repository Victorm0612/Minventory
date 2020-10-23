from django.db import models

class Bill(models.Model):
    bill_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
