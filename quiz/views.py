from rest_framework.response import Response
from rest_framework.decorators import api_view
from .helpers import success,failure
from rest_framework import status

# welcome api page
@api_view(['get'])
def index(request):
    return Response(success(message="Welcome to Quiz API",status=status.HTTP_200_OK))

    def get(self,request):
        try:
            category_obj = Category.objects.all()
            serializer = CategorySerializer(category_obj,many=True)
            return Response(success("Category Fetched Successfully",serializer.data,status.HTTP_200_OK))
        except Exception as ex:
            return Response(failure("Something went wrong",ex))
        
    def post(self,request):
        try:
            data = request.data
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(success("Category Created Successfully",serializer.data,status.HTTP_201_CREATED))
            else:
                return Response(failure(serializer.errors,status.HTTP_400_BAD_REQUEST))
        except Exception as ex:
            return Response(failure(f"Exception: {ex}",status.HTTP_417_EXPECTATION_FAILED))

    def patch(self,request,category_id=None):
        try:
            category_obj = Category.objects.get(_id=category_id)
            category_name = request.data
            serializer = CategorySerializer(category_obj,data=category_name,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(success("Category Updated Successfully",serializer.data,status.HTTP_200_OK))
            else:
                return Response(failure(serializer.errors,status.HTTP_400_BAD_REQUEST))
        except Category.DoesNotExist:
            return Response(failure("Category not found", status.HTTP_404_NOT_FOUND))
        except Exception as ex:
            return Response(failure(f"Exception: {ex}",status.HTTP_417_EXPECTATION_FAILED))

    def delete(self,request,category_id):
        try:
            category_obj = Category.objects.get(_id=category_id)
            category_name = category_obj.category_name  # Get the name of the category for the response message
            category_obj.delete()  # Delete the category
            return Response(success(f"Category '{category_name}' Deleted Successfully", data={}, status=status.HTTP_204_NO_CONTENT))
        except Category.DoesNotExist:
            return Response(failure("Category not found", status.HTTP_404_NOT_FOUND))
        except Exception as ex:
            return Response(failure(f"Exception: {ex}",status.HTTP_417_EXPECTATION_FAILED))
