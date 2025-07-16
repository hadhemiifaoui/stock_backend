
from django.db import models
from .newoutillage import NVoutillage

class OutillageHistory(models.Model):
    outillage = models.ForeignKey(NVoutillage, on_delete=models.CASCADE, related_name='history')
    reference = models.CharField(max_length=255)
    type_outillage = models.CharField(max_length=255)
    date_dentre = models.DateField()
    numero_outillage = models.CharField(max_length=255)
    conformite = models.CharField(max_length=10)
    projet = models.CharField(max_length=255)
    validite_finale = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Historic pour {self.outillage.reference} @ {self.updated_at}"
