from rest_framework.routers import DefaultRouter
from ..views.transaction import TransactionViewSet

router = DefaultRouter()
router.register(r'transactions',TransactionViewSet , basename='transaction')

urlpatterns = router.urls