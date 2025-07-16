from django.db.models.signals import post_delete
from django.dispatch import receiver
from ..models.order import Order
from ..models.stock import Stock

@receiver(post_delete, sender=Order)
def restore_stock_on_order_delete(sender, instance, **kwargs):
    if instance.etat_commande == 'recue' and instance.quantity_cmd:
        try:
            stock = Stock.objects.get(article=instance.article)
        except Stock.DoesNotExist:
            return
        stock.received_commands -= instance.quantity_cmd
        stock.quantity -= instance.quantity_cmd
        stock.save()
