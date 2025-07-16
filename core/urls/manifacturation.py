from rest_framework.routers import DefaultRouter
from ..views.manifacturation import ManifacturationViewSet

router = DefaultRouter()
router.register(r'manifacturationn', ManifacturationViewSet, basename='manifacturation')

urlpatterns = router.urls
