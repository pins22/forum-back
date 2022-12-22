from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "date_joined",
                  "first_name",  "last_name", "username"]


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
