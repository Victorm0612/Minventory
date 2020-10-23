from django.db import models


class Inventory(models.Model):
    date_log = models.DateTimeField(auto_now_add=True)


