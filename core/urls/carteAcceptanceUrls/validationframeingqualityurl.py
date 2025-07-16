from rest_framework.routers import DefaultRouter
from core.views.carteAcceptViews.validationframeingenquality import ValidationFrameIngQualityViewSet

router = DefaultRouter()
router.register(r'validationframeingqual', ValidationFrameIngQualityViewSet, basename='validationframeingqual')

urlpatterns = router.urls
