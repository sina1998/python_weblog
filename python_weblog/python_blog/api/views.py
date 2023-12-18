# python_blog/api/views.py

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from ..models import Post
from rest_framework import viewsets


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePostView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)