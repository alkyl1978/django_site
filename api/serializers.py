from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class SerPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'title', 'content', 'date_create')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('url', 'username', 'email')

