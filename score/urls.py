from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("score", get_user_score, name="get_user_score"),
    path("score-add", add_score, name="add_score")
]