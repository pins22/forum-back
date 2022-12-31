from rest_framework import serializers
from .models import Post, Reply
from users.serializers import UserSerializer
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "date_joined",
                  "first_name",  "last_name", "username"]


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    has_user_upvoted = serializers.SerializerMethodField()
    has_user_downvoted = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'last_changed',
                  'author', 'points', 'has_user_upvoted', 'has_user_downvoted']

    def get_has_user_upvoted(self, obj):
        if not self.context:
            return False
        user = self.context.get("user")
        if user:
            return obj.upvotes.filter(id=user.id).exists()
        return False

    def get_has_user_downvoted(self, obj):
        if not self.context:
            return False
        user = self.context.get("user")
        if user:
            return obj.downvotes.filter(id=user.id).exists()
        return False


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class ReplyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    has_user_upvoted = serializers.SerializerMethodField()
    has_user_downvoted = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'last_changed',
                  'author', 'points', 'has_user_upvoted', 'has_user_downvoted']

    def get_has_user_upvoted(self, obj):
        if not self.context:
            return False
        user = self.context.get("user")
        if user:
            return obj.upvotes.filter(id=user.id).exists()
        return False

    def get_has_user_downvoted(self, obj):
        if not self.context:
            return False
        user = self.context.get("user")
        if user:
            return obj.downvotes.filter(id=user.id).exists()
        return False
