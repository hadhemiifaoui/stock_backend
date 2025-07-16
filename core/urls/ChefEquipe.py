from rest_framework.routers import DefaultRouter
from ..views.ChefEquipe import ChefEquipeViewSet

router = DefaultRouter()
router.register(r'chefequipes', ChefEquipeViewSet)
urlpatterns = router.urls
