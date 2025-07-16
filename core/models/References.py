from django.db import  models
class Reference(models.Model):
    ref = models.CharField(max_length=200 , blank=True)