from rest_framework.routers import DefaultRouter
from ..views.maintenance import MaintenanceViewSet

router = DefaultRouter()
router.register(r'maintenances', MaintenanceViewSet)
urlpatterns = router.urls
