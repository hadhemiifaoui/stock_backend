from rest_framework.routers import DefaultRouter
from ..views.suppliers import SupplierViewSet

router = DefaultRouter()
router.register(r'suppliers',SupplierViewSet , basename='suppliers')

urlpatterns = router.urls
