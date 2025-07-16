from rest_framework.decorators import action
from rest_framework import viewsets
from ..models.stock import Stock
from ..serializers.stockSerializer import StockSerializer
from rest_framework.response import Response
from rest_framework import status
from ..services.stock_services import calculate_virtual_stock
from rest_framework.permissions import IsAuthenticated

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]
    @action(detail=True, methods=['get'], url_path='virtual_stock')
    def calculate_virtual_stock_view(self, request, pk=None):
        try:
            virtual_stock = calculate_virtual_stock(pk)
            if virtual_stock is not None:
                return Response({
                    'message': 'stock virtuelle calculé avec succès.',
                    'virtual_stock': virtual_stock
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'aucune historique de stock pour la semaine dernière ou stock non trouvé'
                }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
