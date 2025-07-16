

from django.db.models.signals import pre_delete
from django.dispatch import receiver
from ..models.inventory import Inventory
from ..services.stock_services import update_stock_quantity

@receiver(pre_delete, sender=Inventory)
def reverse_stock_on_inventory_delete(sender, instance, **kwargs):

    if instance.stock:
        update_stock_quantity(
            stock_id=instance.stock.id,
            quantity_added=-instance.quantity_added,
            quantity_removed=-instance.quantity_removed,
            quantity_produced=-getattr(instance, 'quantity_produced', 0),
            quantite_consume=-getattr(instance, 'quantite_consume', 0)
        )
