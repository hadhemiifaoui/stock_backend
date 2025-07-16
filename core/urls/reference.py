from rest_framework.routers import DefaultRouter
from ..views.reference import ReferenceViewSet

router = DefaultRouter()
router.register(r'references', ReferenceViewSet, basename='references')

urlpatterns = router.urls
