from django.db import models
from .stock import Stock
from .article import Article
class HistoriqueStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,related_name='historique_entries')
    quantity = models.IntegerField(default=0)
    received_commands = models.IntegerField(default=0)
    total_quantity_used = models.IntegerField(default=0)
    consomation_annuelle = models.IntegerField(blank=True, null=True)
    location = models.CharField(
        max_length=50,
        choices=[('Block A', 'Block A'), ('Block B', 'Block B'), ('Block A/B', 'Block A/B')],
        blank=True
    )

    reorder_level = models.IntegerField(blank=True, null=True)
    delai_approvisionnement = models.CharField(max_length=100,
                                               choices=[('1 semaine', '1 semaine'),
                                                        ('2 semaines', '2 semaines'), ('3 semaines', '3 semaines'),
                                                        ('4 semaines', '4 semaines'),
                                                        ('5 semaines', '5 semaines'), ('6 semaines', '6 semaines'),
                                                        ('7 semaines', '7 semaines'),
                                                        ('8 semaines', '8 semaines'), ('9 semaines', '9 semaines'),
                                                        ('10 semaines', '10 semaines'),
                                                        ('11 semaines', '11 semaines')
                                                   , ('12 semaines', '12 semaines')],
                                               default="1 semaine",
                                               blank=True
                                               , null=True)
    seuil_min = models.IntegerField(default=0, blank=True, null=True)
    virtual_stock = models.IntegerField(blank=True, null=True)
    ecart_stock = models.IntegerField(blank=True, null=True)
    a_commande = models.IntegerField(blank=True, default=0)

    updated_at = models.DateField(auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"Historic pour {self.stock.article.name} @ {self.updated_at}"
