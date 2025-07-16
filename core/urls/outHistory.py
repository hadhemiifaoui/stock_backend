
from django.urls import path
from ..views.outillageHistory import OutillageHistoryListView
from rest_framework.routers import DefaultRouter
from ..views.outillageHistory import OutillageHistory

router = DefaultRouter()
router.register(r'outhistory', OutillageHistory, basename='outhistory')

urlpatterns = router.urls + [
    path('outhistory/<int:outillage_id>/history/', OutillageHistoryListView.as_view(), name='outillage-history'),
]
