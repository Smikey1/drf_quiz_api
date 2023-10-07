from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
    # path("user/login", obtain_auth_token, name="login"),
    path("user/login", user_login_view, name="login_user"),
    path("user/logout", user_logout_view, name="logout_user"),
    path("user/register", user_register_view, name="register"),
    path("user/profile", user_profile_view, name="profile"),
    path("score", get_user_score, name="get_user_score"),
    path("score-add", add_score, name="add_score")
]