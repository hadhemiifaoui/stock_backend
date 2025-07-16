from django.db import models
from .user import User

class Report(models.Model):
    report_date = models.DateField()
    planned_date = models.DateField()
    filePath = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    report_type  = models.CharField(max_length=100)
    report_category = models.CharField(max_length=100)
    generatedBy = models.ForeignKey(User , on_delete=models.CASCADE)


    def __str__(self):
        return self.report_type