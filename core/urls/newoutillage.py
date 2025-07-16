# from rest_framework.routers import DefaultRouter
# from ..views.NewOutillage import NVoutillageViewSet
#
# router = DefaultRouter()
# router.register(r'newoutillage', NVoutillageViewSet, basename='newoutillage')
# urlpatterns = router.urls


from django.urls import path
from rest_framework.routers import DefaultRouter
from ..views.NewOutillage import NVoutillageViewSet
from ..views.outillageHistory import OutillageHistoryListView

router = DefaultRouter()
router.register(r'newoutillage', NVoutillageViewSet, basename='newoutillage')

urlpatterns = router.urls + [
    path('outhistory/<int:outillage_id>/history/', OutillageHistoryListView.as_view(), name='outillage-history'),
]
