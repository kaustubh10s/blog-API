from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Post
from .permissions import IsAuthorOrReadOnly 
from .serializers import PostSerializer, UserSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = (permissions.IsAdminUser,) # only admin can view the post-details page


class UserList(generics.ListCreateAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer