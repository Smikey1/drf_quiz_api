from rest_framework import serializers
from .models import ScoreModel

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreModel
        fields = "__all__"