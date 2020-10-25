from django.db import models


# Create your models here.
class RequestQuotation(models.Model):
    RANGE_1 = "8:00 - 9:30"
    RANGE_2 = "10:00 - 11:30"
    RANGE_3 = "13:00 - 14:30"
    RANGE_4 = "15:00 - 16:30"
    RANGE_5 = "17:00 - 18:30"

    RANGES = ((RANGE_1, 1), (RANGE_2, 2), (RANGE_3, 3), (RANGE_4, 4), (RANGE_5, 5))
    # La @request_date se autogenera al momento de pedir la cita
    request_date = models.DateTimeField(auto_now_add=True)

    # la @scheduled_date es la que el cliente debe asignarle
    # Formato: YYYY-MM-DD
    scheduled_date = models.DateField()
    time_range = models.TextField(max_length=13,choices=RANGES)
    approved = models.BooleanField()
    service_type = models.TextField(max_length=50)
    description = models.TextField(max_length=200)
    fkUser_int = models.IntegerField()