from rest_framework.routers import DefaultRouter
from ..views.role import RoleViewSet

router = DefaultRouter()
router.register(r'role', RoleViewSet, basename='role')
urlpatterns = router.urls
