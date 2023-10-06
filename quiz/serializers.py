from rest_framework import serializers
from .models import *
import re as regex
class CategorySerializer(serializers.ModelSerializer):
    def validate(self, data):
        category_name = data.get("category_name")
        if category_name:
            pattern = regex.compile("[@_!#$%^&*()<>?/|}{~:]")
            if len(category_name)<3:
                raise serializers.ValidationError("Cagetory Name must be greater than 3 char")
            if not pattern.search(category_name)==None:
                raise serializers.ValidationError("Category Name connot contain special Character")
            return data

    class Meta:
        model = Category
        exclude = ["created_at","updated_at"]