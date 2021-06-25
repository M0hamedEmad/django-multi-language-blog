from django.urls import path
from .views import PostList, PostDetail, CommentDelete

app_name = 'post'

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('comment/delete/<int:pk>', CommentDelete.as_view(), name='delete_comment'),
    path('<slug:slug>/', PostDetail.as_view(), name='post'),
]