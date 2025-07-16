from rest_framework.routers import DefaultRouter
from ..views.test import TestViewSet

router = DefaultRouter()
router.register(r'tests',TestViewSet , basename='tests')

urlpatterns = router.urls
