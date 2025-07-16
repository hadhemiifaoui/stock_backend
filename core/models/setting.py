from django.db import models
from .user import User
class Setting(models.Model):
    settingKey = models.CharField(max_length=100)
    settingValues = models.CharField(max_length=100)
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    notes = models.CharField(max_length=100)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  self.settingKey