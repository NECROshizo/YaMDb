from django.urls import include, path
from rest_framework import routers

from .views import (
    ReviewsViewSet,
    CommentViewSet,
)
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('users.urls')),
]
