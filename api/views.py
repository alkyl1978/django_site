# -*- coding: utf-8 -*

from blog.models import Post
from .serializers import SerPost, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers import *

class PostList(ModelViewSet):
    serializer_class = SerPost
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser,)

class UserList(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
