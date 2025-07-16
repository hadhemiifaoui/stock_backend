from rest_framework.routers import DefaultRouter
from core.views.carteAcceptViews.validationoutillageserviceoutillage import ValidationOutillageServiceOutillageViewSet

router = DefaultRouter()
router.register(r'validationoutillageservoutillage', ValidationOutillageServiceOutillageViewSet, basename='validationoutillageservoutillage')

urlpatterns = router.urls
