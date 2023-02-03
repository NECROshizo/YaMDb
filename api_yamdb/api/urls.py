from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/', include(router.urls))
]
