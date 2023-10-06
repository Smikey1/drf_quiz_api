from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# creating default router
router = DefaultRouter()
router.register("id",CategoryViewSet,basename="category")

# creating endpoints
urlpatterns = [
    path('', index, name="index"),
    path('category', CategoryView.as_view()),
    path('category/<str:category_id>', CategoryView.as_view()),
    path('category', include(router.urls)),
    path('question', QuestionAPIView.as_view()),
]

# urlpatterns += router.urls