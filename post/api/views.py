from django.utils.timezone import now
from django.db.models import Q
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView
    )
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from post.models import Post, Comment
from .serializers import (
    PostSerializer,
    PostDetailSerializer,
    PostCommentSerailzer,
    CommentSerailzer
    )
from .permissions import IsAuthorOrReadOnly, IsOwnerOrReadOnly

class PostAPIView(ListCreateAPIView):
    queryset = Post.objects.filter( Q(active=True) & Q(published_at__lte=now()) )
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter( Q(active=True) & Q(published_at__lte=now()) )
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    lookup_field = 'slug'


class CommentCreateApiView(CreateAPIView):
    model = Comment
    serializer_class = PostCommentSerailzer
    permission_classes = [IsAuthenticated,]


    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        post = Post.objects.get(slug=slug)

        serializer.save(user=self.request.user, post=post)


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerailzer
    

class CommentDetialAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerailzer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
