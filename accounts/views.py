from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .helpers import success,failure
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.generics import ListAPIView


@api_view(["POST"])
def user_logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(success(message= "You are logged out", status=status.HTTP_200_OK))

@api_view(["POST"])
def user_register_view(request):
    serializer = UserRegisterSerializer(data=request.data)    
    data = {} 
    if serializer.is_valid():
        account = serializer.save()
        
        data['username'] = account.username
        data['email'] = account.email
        
        return Response(success(message= "User Register Successfully",data=data, status=status.HTTP_200_OK))
    else:
        data = serializer.errors["username"][0]
        return Response(failure(message= data, status=status.HTTP_400_BAD_REQUEST))


@api_view(["POST"])
def user_login_view(request):
    # Get the username and password from the request data
    username = request.data.get("username")
    password = request.data.get("password")

    # Authenticate the user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # If authentication is successful, generate tokens
        # token = Token.objects.get(user=account).key
        # data['token'] = token
        
        # data['token'] = {
        #     'refresh_token': str(refresh),
        #     'access_token': str(refresh.access_token)
        # }

        
        refresh = RefreshToken.for_user(user)
        
        data = {
            "fullname": f"{user.first_name} {user.last_name}",
            'username': user.username,
            'email': user.email,
            'token': {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }
        }
        return Response(success(message="Login Successful", data=data, status=status.HTTP_200_OK))
    else:
        return Response(failure(message="Invalid credentials", status=status.HTTP_401_UNAUTHORIZED))

@api_view(["GET"])
@permission_classes([IsAuthenticated])  # Ensure that only authenticated users can access this view
def user_profile_view(request):
    try:
        # Get the profile of the currently authenticated user
        user_profile = UserProfile.objects.get(user=request.user)

        # Serialize the user profile data
        serializer = UserProfileSerializer(user_profile)

        return Response(success(message="User profile retrieved successfully", data=serializer.data, status=status.HTTP_200_OK))
    except UserProfile.DoesNotExist:
        return Response(failure(message="User profile not found", status=status.HTTP_404_NOT_FOUND))

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_score(request):
    try:
        # Retrieve scores for the authenticated user's user profile
        user_scores = request.user.userprofile.scores.all()
        # user_scores = ScoreModel.objects.filter(user=request.user)
        serializer = ScoreSerializer(user_scores, many=True)
        return Response(success("All Scores Fetched Successfully", serializer.data, status.HTTP_200_OK))
    except ScoreModel.DoesNotExist:
        return Response(failure("No scores found for the user", status.HTTP_404_NOT_FOUND))
    except Exception as ex:
        return Response(failure("Failed to get scores", status.HTTP_500_INTERNAL_SERVER_ERROR))


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_score(request):
    try:
        # Retrieve the authenticated user's user profile
        user_profile = request.user.userprofile

        # Get the score data from the request data
        score_data = {
            'user': user_profile._id,
            'score_value': request.data.get('score_value', 0)  # You can change the field name as needed
        }

        # Create a new score instance
        score_serializer = ScoreSerializer(data=score_data)
        if score_serializer.is_valid():
            score_serializer.save()
            return Response(success(message="Score added successfully", status=status.HTTP_201_CREATED))
        else:
            return Response(failure("Invalid score data", status.HTTP_400_BAD_REQUEST))
    except Exception as ex:
        return Response(failure("Failed to add score", status.HTTP_500_INTERNAL_SERVER_ERROR))