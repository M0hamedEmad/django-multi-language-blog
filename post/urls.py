from django.urls import path
from .views import PostList, PostDetail

app_name = 'post'

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post'),
]