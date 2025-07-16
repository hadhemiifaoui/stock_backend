from rest_framework.routers import DefaultRouter
from core.views.carteAcceptViews.validationframeserviceoutillage import ValidationFrameServiceOutillageViewSet

router = DefaultRouter()
router.register(r'validationframeserviceoutillage', ValidationFrameServiceOutillageViewSet, basename='validationframeserviceoutillage')

urlpatterns = router.urls
