from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    queryset = User.objects.all()