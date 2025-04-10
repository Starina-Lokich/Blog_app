from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # Указываем модель Post
        fields = ['id', 'title', 'content', 'created_at', 'author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  # Указываем модель Comment
        fields = ['id', 'post', 'text', 'created_at']
        