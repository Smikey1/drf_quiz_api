from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .helpers import success,failure
from rest_framework import status
from .models import *
from .serializers import *

# welcome api page
@api_view(['get'])
def index(request):
    return Response(success(message="Welcome to Quiz API",status=status.HTTP_200_OK))


class CategoryView(APIView):
    def get(self,request):
        try:
            category_obj = Category.objects.all()
            serializer = CategorySerializer(category_obj,many=True)
            return Response(success("Category Fetched Successfully",serializer.data,status.HTTP_200_OK))
        except Exception as ex:
            return Response(failure("Something went wrong",ex))
        