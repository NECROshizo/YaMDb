from django.urls import include, path

from users.views import get_token, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('token/', get_token, name='get_token'),
]
