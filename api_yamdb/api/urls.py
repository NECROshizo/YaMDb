from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet
from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/', include(router.urls))
]
