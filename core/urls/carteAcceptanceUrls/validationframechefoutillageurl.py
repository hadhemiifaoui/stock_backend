# from rest_framework.routers import DefaultRouter
# from core.views.carteAcceptViews.validationframechefoutillage import ValidationFrameChefOutillageViewSet
#
# router = DefaultRouter()
# router.register(r'validationframechefOut', ValidationFrameChefOutillageViewSet, basename='validationframechefOut')
#
# urlpatterns = router.urls




from rest_framework.routers import DefaultRouter
from core.views.carteAcceptViews.validationframechefoutillage import ValidationFrameChefOutillageViewSet
from django.urls import path, include
from core.views.socket import validation_frame_alerts
router = DefaultRouter()

router.register(r'validationframechefOut',ValidationFrameChefOutillageViewSet , basename='validationframechefOut')

urlpatterns = [
    path('alerts/', validation_frame_alerts, name='alerts'),
    path('', include(router.urls)),
]


























































































































































