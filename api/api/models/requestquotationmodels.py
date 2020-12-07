from django.db import models
from api.models.usermodels import User
from api.models.statusmodels import Status


class RequestQuotation(models.Model):
    RANGE_1 = "08:00 - 09:30"
    RANGE_2 = "10:00 - 11:30"
    RANGE_3 = "13:00 - 14:30"
    RANGE_4 = "15:00 - 16:30"
    RANGE_5 = "17:00 - 18:30"
    RANGES = ((RANGE_1, 1), (RANGE_2, 2), (RANGE_3, 3), (RANGE_4, 4), (RANGE_5, 5))

    request_date = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateField()
    time_range = models.TextField(max_length=13,choices=RANGES)
    approved = models.BooleanField()
    service_type = models.TextField(max_length=50)
    description = models.TextField(max_length=200)
    fkUser_id = models.ForeignKey(User, related_name='User_id', on_delete=models.CASCADE)
    fkTask_status = models.ForeignKey(Status, related_name='Status_id', on_delete=models.CASCADE)

    def update_field(self, key, value):
        getattr(self, key)
        if key not in ('fkUser_id', 'scheduled_date', 'request_date', 'approved', 'fkTask_status'):
            setattr(self, key, value)