from django.db import models

class Test(models.Model):
    data_di_controllo = models.DateField(null=True, blank=True)
    plant_manager = models.CharField(max_length=255 , blank=True)
    reference = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    wip_name = models.CharField(max_length=255)
    quantity_of_defects = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    descrizione_defects = models.TextField()
    kind_of_defect = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.reference} - {self.kind_of_defect}"
