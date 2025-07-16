from rest_framework.routers import DefaultRouter
from core.views.carteAcceptViews.validationoutillageingquality import ValidationOutillageIgenQualityViewSet

router = DefaultRouter()
router.register(r'validationoutillageingqual', ValidationOutillageIgenQualityViewSet, basename='validationoutillageingqual')

urlpatterns = router.urls
