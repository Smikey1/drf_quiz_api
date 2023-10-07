from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScoreSerializer
from .helpers import success,failure
from rest_framework.permissions import IsAuthenticated
from .models import ScoreModel


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
        return Response(failure(message="No scores found for the user", status=status.HTTP_404_NOT_FOUND))
    except Exception as ex:
        return Response(failure(message="Failed to get scores", status=status.HTTP_500_INTERNAL_SERVER_ERROR))


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
            return Response(failure(message="Invalid score data", status= status.HTTP_400_BAD_REQUEST))
    except Exception as ex:
        return Response(failure(message="Failed to add score", status=status.HTTP_500_INTERNAL_SERVER_ERROR))