from rest_framework.routers import DefaultRouter
from core.views.carteAcceptViews.accepteCarte import AcceptCarteViewSet

router = DefaultRouter()
router.register(r'acceptecarte', AcceptCarteViewSet, basename='acceptecarte')

urlpatterns = router.urls
