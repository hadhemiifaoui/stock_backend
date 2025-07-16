from rest_framework.routers import DefaultRouter
from ..views.planning import PlanningViewSet

router = DefaultRouter()
router.register(r'planning', PlanningViewSet, basename='planning')

urlpatterns = router.urls
