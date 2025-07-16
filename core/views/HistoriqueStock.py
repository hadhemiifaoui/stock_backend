# from rest_framework import viewsets
# from ..models.HistoriqueStock import HistoriqueStock
# from ..serializers.HistoriqueStockSerializer import HistoriqueStockSerializer

# class HistoriqueStockViewSet(viewsets.ModelViewSet):
#     queryset = HistoriqueStock.objects.all()
#     serializer_class = HistoriqueStockSerializer


from rest_framework import generics
from ..models.HistoriqueStock import HistoriqueStock
from ..serializers.HistoriqueStockSerializer import HistoriqueStockSerializer

class HistoriqueStockViewSet(generics.ListAPIView):
    serializer_class = HistoriqueStockSerializer

    def get_queryset(self):
        stock_id = self.kwargs['stock_id']
        return HistoriqueStock.objects.filter(stock_id=stock_id).order_by('-updated_at')
