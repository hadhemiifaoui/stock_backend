from django.db import  models
class Project(models.Model):
    proj_ref = models.CharField(max_length=200 , blank=True)