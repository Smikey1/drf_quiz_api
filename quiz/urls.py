from django.urls import path
from .views import *

# creating endpoints
urlpatterns = [
    path('', index, name="index"),
]

# urlpatterns += router.urls