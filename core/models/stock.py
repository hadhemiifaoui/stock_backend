from django.db import models
from django.core.exceptions import ValidationError
from .article import Article
from simple_history.models import HistoricalRecords

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class Stock(models.Model):
    quantity = models.IntegerField(default=0)
    received_commands = models.IntegerField(default=0)
    total_quantity_used = models.IntegerField(default=0)
    consomation_annuelle = models.IntegerField(blank=True, null=True)
    location = models.CharField(
        max_length=50,
        choices=[('Block A', 'Block A'), ('Block B', 'Block B'),('Block A/B', 'Block A/B')],
        blank=True
    )

    reorder_level = models.IntegerField(blank=True, null=True)
    delai_approvisionnement = models.CharField(  max_length=100,
        choices=[('1 semaine', '1 semaine'),
                 ('2 semaines', '2 semaines'), ('3 semaines', '3 semaines'), ('4 semaines', '4 semaines'),
                 ('5 semaines', '5 semaines'), ('6 semaines', '6 semaines'), ('7 semaines', '7 semaines'),
                 ('8 semaines', '8 semaines'), ('9 semaines', '9 semaines'), ('10 semaines', '10 semaines'),
                 ('11 semaines', '11 semaines')
            , ('12 semaines', '12 semaines')],
           default="1 semaine",
        blank=True
        ,null=True)
    seuil_min = models.IntegerField(default=0 , blank=True ,null=True)
    virtual_stock = models.IntegerField(blank=True, null=True)
    ecart_stock = models.IntegerField(blank=True, null=True)
    a_commande = models.IntegerField(blank=True, default=0)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)


    history = HistoricalRecords()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(quantity__gte=0), name='quantity_non_negative'),
            models.CheckConstraint(check=models.Q(total_quantity_used__gte=0), name='used_quantity_non_negative'),
            models.UniqueConstraint(fields=['article'], name='unique_article_in_stock'),
        ]

    def save(self, *args, **kwargs):

        if not self.pk and Stock.objects.filter(article=self.article).exists():
            raise ValidationError(f" article '{self.article.name}' already has stock registered")


        self.virtual_stock = self.quantity - self.total_quantity_used + self.received_commands
        self.ecart_stock = self.virtual_stock - self.quantity

        if self.virtual_stock <= self.seuil_min:
            self.a_commande = int((self.seuil_min - self.virtual_stock) + self.seuil_min * 0.5)
            if self.a_commande > 0:
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "stock_alerts",
                    {
                        "type": "stock_alert",
                        "message": f"Stock for '{self.article.name}' is below minimum: {self.virtual_stock} units left (min: {self.seuil_min}): U have to commande {self.a_commande}"
                    },
                )
        else:
            self.a_commande = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Stock for {self.article.name}"




 # a_commande tet7seb ml stock_virtuelle








    # def save(self, *args, **kwargs):
    #     if not self.pk and Stock.objects.filter(article=self.article).exists():
    #         raise ValidationError(f"Article '{self.article.name}' already has stock registered")
    #
    #     self.virtual_stock = self.quantity - self.total_quantity_used + self.received_commands
    #     self.ecart_stock = self.virtual_stock - self.quantity
    #
    #     if self.seuil_min != 0 and self.quantity != 0:
    #         if self.virtual_stock <= self.seuil_min:
    #             commande_value = (self.seuil_min - self.virtual_stock) + self.seuil_min * 0.5
    #             self.a_commande = int(commande_value) if commande_value > 0 else 0
    #
    #             if self.a_commande > 0:
    #                 channel_layer = get_channel_layer()
    #                 async_to_sync(channel_layer.group_send)(
    #                     "stock_alerts",
    #                     {
    #                         "type": "stock_alert",
    #                         "message": (
    #                             f"Stock for '{self.article.name}' is below minimum: "
    #                             f"{self.quantity} units left (min: {self.seuil_min}). "
    #                             f"Vous devez commander {self.a_commande}."
    #                         )
    #                     },
    #                 )
    #         else:
    #             self.a_commande = 0
    #     else:
    #         self.a_commande = 0
    #
    #     super().save(*args, **kwargs)
