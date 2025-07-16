from django.db import models
from .user import User
from .article import Article
class Maintenance(models.Model):
    maint_type = models.CharField(
        max_length=50,
        choices=[('maintenance préventive', 'maintenance préventive'),
                 ('maintenance curative', 'maintenance curative')],
        blank=True
    )
    statut = models.CharField(
        max_length=100,
        choices=[('Valide', 'Valide'),
                 ('Invalide', 'Invalide'),
                ],
        default='Invalide',
        blank=True
        ,null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    articles = models.ManyToManyField(Article,through='MaintenanceArticle', blank=True)

    class Meta:
        abstract = False

class MaintenanceArticle(models.Model):
    maintenance = models.ForeignKey('Maintenance', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite_consume = models.IntegerField(blank=True)
