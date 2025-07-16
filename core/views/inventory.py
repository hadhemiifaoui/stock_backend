from rest_framework import viewsets
from ..models.inventory import Inventory
from ..serializers.inventorySerializer import InventorySerializer
from ..services.stock_services import update_stock_quantity
from rest_framework.permissions import IsAuthenticated
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        inventory = serializer.save()

        update_stock_quantity(
            inventory.stock.id,
            quantity_added=inventory.quantity_added,
            quantity_removed=inventory.quantity_removed
        )

    def perform_update(self, serializer):
        inventory = serializer.save()
        update_stock_quantity(
            inventory.stock.id,
            quantity_added=inventory.quantity_added,
            quantity_removed=inventory.quantity_removed
        )

