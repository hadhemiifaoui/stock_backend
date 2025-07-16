from rest_framework.routers import DefaultRouter
from ..views.articles import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = router.urls
