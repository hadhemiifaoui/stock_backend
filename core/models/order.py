# from django.db import models
# from .article import Article
# from .supplier import Supplier
# from .stock import Stock
#
#
# class Order(models.Model):
#     date_commande = models.DateField(null=True, blank=True)
#     date_livraison = models.DateField(null=True, blank=True)
#     etat_commande = models.CharField(choices=[('commandé', 'commandé'),
#                                               ('a commandé', 'a commandé'),
#                                               ('recue', 'recue')
#                                               ], default="a commandé", max_length=50, blank=True)
#     quantity_cmd = models.IntegerField(null=True,blank=True)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE ,null=True, blank=True)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE , null=True, blank=True)
#     createdAt = models.DateField(auto_now_add=True)
#     updatedAt = models.DateField(auto_now=True)
#
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             if self.etat_commande == 'recue':
#                 try:
#                     stock = Stock.objects.get(article=self.article)
#                     print(f"Creating new order with 'recue' status for article: {self.article.name}")
#
#                     stock.received_commands += self.quantity_cmd
#                     stock.virtual_stock += self.quantity_cmd
#                     print(f"New received_commands: {stock.received_commands}, New stock quantity: {stock.virtual_stock}")
#
#                     stock.save()
#
#                 except Stock.DoesNotExist:
#                     print(f"No stock found for article: {self.article.name}.")
#         else:
#             previous = Order.objects.get(pk=self.pk)
#             if previous.etat_commande != 'recue' and self.etat_commande == 'recue':
#                 try:
#                     stock = Stock.objects.get(article=self.article)
#                     print(f"Updating stock for article: {self.article.name}")
#
#                     stock.received_commands += self.quantity_cmd
#                     stock.virtual_stock += self.quantity_cmd
#                     print(
#                         f"Updated received_commands: {stock.received_commands}, "
#                         f"Updated stock quantity: {stock.quantity}")
#
#                     stock.save()
#
#                 except Stock.DoesNotExist:
#                     print(f"No stock found for article: {self.article.name}.")
#             elif previous.quantity_cmd != self.quantity_cmd and self.etat_commande == 'recue':
#                 try:
#                     stock = Stock.objects.get(article=self.article)
#                     print(
#                         f"Updating stock for article: {self.article.name}, "
#                         f"previous received_commands: {stock.received_commands}")
#
#                     stock.received_commands -= previous.quantity_cmd
#                     stock.received_commands += self.quantity_cmd
#
#                     stock.virtual_stock -= previous.quantity_cmd
#                     stock.virtual_stock += self.quantity_cmd
#                     print(
#                         f"Updated received_commands: {stock.received_commands}, "
#                         f"Updated stock quantity: {stock.virtual_stock}")
#
#                     stock.save()
#
#                 except Stock.DoesNotExist:
#                     print(f"No stock found for article: {self.article.name}.")
#
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return f"Commande de {self.article.name} - {self.etat_commande}"



from django.db import models
from .article import Article
from .supplier import Supplier
from .stock import Stock

class Order(models.Model):
    date_commande = models.DateField(null=True, blank=True)
    date_livraison = models.DateField(null=True, blank=True)
    etat_commande = models.CharField(
        choices=[
            ('commandé', 'commandé'),
            ('a commandé', 'a commandé'),
            ('recue', 'recue')
        ],
        default="a commandé",
        max_length=50,
        blank=True
    )
    quantity_cmd = models.IntegerField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        previous_quantity = 0
        was_received = False


        if not is_new:
            previous_order = Order.objects.get(pk=self.pk)
            previous_quantity = previous_order.quantity_cmd or 0
            was_received = previous_order.etat_commande == 'recue'

        super().save(*args, **kwargs)

        try:
            stock = Stock.objects.get(article=self.article)
        except Stock.DoesNotExist:
            print(f"No stock found for article: {self.article.name}")
            return

        # Add to stock if new order marked as 'recue'
        if is_new and self.etat_commande == 'recue':
            stock.received_commands += self.quantity_cmd
            stock.virtual_stock += self.quantity_cmd
            print(f"[NEW] Added {self.quantity_cmd} to received_commands and virtual_stock")

        elif not is_new and not was_received and self.etat_commande == 'recue':
            stock.received_commands += self.quantity_cmd
            stock.virtual_stock += self.quantity_cmd
            print(f"[STATUS CHANGE] Added {self.quantity_cmd} to received_commands and virtual_stock")

        elif not is_new and was_received and self.etat_commande == 'recue':
            delta = self.quantity_cmd - previous_quantity
            stock.received_commands += delta
            stock.virtual_stock += delta
            print(f"[QUANTITY CHANGE] Adjusted by {delta} in received_commands and virtual_stock")

        stock.save()

    def __str__(self):
        return f"Commande de {self.article.name} - {self.etat_commande}"
