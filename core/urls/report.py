from rest_framework.routers import DefaultRouter
from ..views.report import ReportViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet, basename='reports')

urlpatterns = router.urls
