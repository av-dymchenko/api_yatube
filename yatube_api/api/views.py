from rest_framework import viewsets
from posts.models import Post, Group
from .serializeres import PostSerializer, CommentSerializer, GroupSerializer
from django.shortcuts import get_object_or_404
from api.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

PERMISSIONS = [IsAuthenticated, IsAuthorOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = PERMISSIONS

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = PERMISSIONS

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_pk'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
