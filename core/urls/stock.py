

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.stock import StockViewSet
from ..views.socket import low_stock_alerts
from ..views.HistoriqueStock import HistoriqueStockViewSet
router = DefaultRouter()
router.register(r'stock', StockViewSet, basename='stock')

urlpatterns = [
    path('low-stock-alerts/', low_stock_alerts, name='low-stock-alerts'),
    path('stockhistory/<int:stock_id>/history/',  HistoriqueStockViewSet.as_view(), name='stock-historique'),
    path('', include(router.urls)),
]
