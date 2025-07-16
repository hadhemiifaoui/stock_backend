from rest_framework import viewsets
from ..models.transaction import Transaction
from ..services.stock_services import update_stock_quantity
from ..serializers.transactionSerializer import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        transaction = serializer.save()

        update_stock_quantity(
            transaction.stock.id,
            quantity_transacted=transaction.quantity_transacted,
            #quantity_removed=inventory.quantity_removed
        )

    def perform_update(self, serializer):
        transaction = serializer.save()
        update_stock_quantity(
            transaction.stock.id,
            quantity_transacted=transaction.quantity_transacted,
           # quantity_removed=inventory.quantity_removed
        )