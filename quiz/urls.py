from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# creating default router
router = DefaultRouter()

# creating endpoints
urlpatterns = [
    path('', index, name="index"),
    path('category', CategoryView.as_view())
]

# urlpatterns += router.urls