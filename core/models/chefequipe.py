from django.db import  models

class ChefEquipe(models.Model):
    nom = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=200, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return f'nom de chef dequipe est :'+self.nom+'.'