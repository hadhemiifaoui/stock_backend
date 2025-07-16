

from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.JSONField(default=dict)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name