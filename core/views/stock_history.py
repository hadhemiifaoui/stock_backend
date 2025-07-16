from rest_framework import viewsets
from ..models.stock_history import StockHistory
from ..serializers.stockHistorySerializer import StockHistorySerializer

class StockHistoryViewSet(viewsets.ModelViewSet):
    queryset = StockHistory.objects.all()
    serializer_class = StockHistorySerializer

