from django.db import models

class Supplier(models.Model):
    nom= models.CharField(max_length=150)
    tel = models.CharField(max_length=100 ,blank=True)
    email = models.CharField(max_length=100 ,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'le contact de fournisseur {self.nom} est :  {self.tel} et {self.email}'