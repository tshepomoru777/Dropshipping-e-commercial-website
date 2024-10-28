from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Comment  # Assuming these models exist

User = get_user_model()

class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'salt']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is not returned in responses
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            salt=validated_data['salt']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

# Add ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'totalprice', 'saleprice', 'discount', 'title', 'description', 'image']

# Add CommentSerializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate', 'users', 'product', 'created_at']