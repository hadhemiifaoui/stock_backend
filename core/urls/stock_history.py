from rest_framework.routers import DefaultRouter
from ..views.stock_history import StockHistoryViewSet

router = DefaultRouter()
router.register(r'stock-history', StockHistoryViewSet, basename='stock-history')
urlpatterns = router.urls
