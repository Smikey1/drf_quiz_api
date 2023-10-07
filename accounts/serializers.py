from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .helpers import success,failure
from .models import *
import uuid as unique_id
from django.utils import timezone

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'confirm_password'}, write_only=True)
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ["first_name",'last_name','username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']

        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError(failure(message="Email already exist",status=status.HTTP_400_BAD_REQUEST))
                
        if password != confirm_password:
            raise serializers.ValidationError(failure(message="Password Does not match",status=status.HTTP_400_BAD_REQUEST))
        

                
        # Create the User instance
        # Create the User instance with first_name and last_name
        user = User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        # Create the UserProfile instance and associate it with the User
        full_name = f'{first_name} {last_name}'
        avatarUrl = rf'https://ui-avatars.com/api/?background=random&name=${full_name}'

        # Get the current date and time in the UTC time zone
        current_datetime_utc = timezone.now()

        # Format the datetime as a string with only the date
        formatted_date = current_datetime_utc.strftime("%Y-%m-%d")

        # Create the UserProfile instance and associate it with the User
        user_profile = UserProfile(
            user=user,
            _id=unique_id.uuid4(),
            first_name=first_name,
            last_name=last_name,
            email=email,
            profile_url=avatarUrl, # Use the provided profile_url or an empty string
            created_at=formatted_date,  # Set created_at to the current date
            updated_at=formatted_date
        )
        user_profile.save()

        return user


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreModel
        fields = "__all__"