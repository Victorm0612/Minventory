from django.db import models


class Status(models.Model):
    description = models.TextField()