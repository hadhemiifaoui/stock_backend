# from django.db import models
# from .user import User
# class Availability(models.Model):
#     fabriqueur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availabilities')
#     weekday = models.IntegerField(choices=[(i, f"S{i}") for i in range(1,8)], null=True, blank=True)
#     date_from = models.DateField(null=True, blank=True)
#     date_to = models.DateField(null=True, blank=True)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#     class Meta:
#         unique_together = ('fabriqueur', 'weekday', 'start_time', 'end_time')



from django.db import models
from .user import User

class Availability(models.Model):
    fabriqueur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availabilities')
    weekday = models.IntegerField(choices=[(i, f"S{i}") for i in range(1, 8)])
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('fabriqueur', 'weekday', 'start_time', 'end_time')

