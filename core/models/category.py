from django.db import models
class Category(models.Model):
    nom = models.CharField(max_length=200)
    desc = models.CharField(max_length=200 , blank=True)

    def __str__(self):
        return self.nom