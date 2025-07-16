from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.user import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('signup/', UserViewSet.as_view({'post': 'signup'}), name='signup'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('', include(router.urls)),
]

#/ --> raj3iha 9bal sighup and login !!!!!