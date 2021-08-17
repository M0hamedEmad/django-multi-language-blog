from django.urls import path
from .views import (
        PostAPIView, 
        PostDetailAPIView,
        CommentCreateApiView,
        CommentListAPIView,
        CommentDetialAPIView
        )


app_name = 'post_api'

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('posts/<slug:slug>/', PostDetailAPIView.as_view(), name='post'),
    path('posts/<slug:slug>/comment/', CommentCreateApiView.as_view(), name='create_comment'),
    path('comments/', CommentListAPIView.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetialAPIView.as_view(), name='comment'),

]
