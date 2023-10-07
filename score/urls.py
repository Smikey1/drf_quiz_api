from django.urls import path
from .views import *

urlpatterns = [
    path("score", get_user_score, name="get_user_score"),
    path("score-add", add_score, name="add_score")
]