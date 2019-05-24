from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user']
        user = serializers.ReadOnlyField(source='user.username')

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.user = validated_data.get('user', instance.user)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['username', 'name', 'email']


