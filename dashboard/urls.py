from django.urls import path
from  .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CommentListView,
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    )

app_name = 'dashboard'

urlpatterns = [
    # Post Urls
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    
    # Categories Urls
    path('category/', CategoryListView.as_view(), name='categories'),
    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    
    # Comments Urls
    path('comment/', CommentListView.as_view(), name='comments'),
    
    # Accounts Urls
    path('account/', AccountListView.as_view(), name='accounts'),
    path('account/create/', AccountCreateView.as_view(), name='accounts_create'),
    path('account/update/<int:pk>/', AccountUpdateView.as_view(), name='accounts_update'),
    path('account/delete/<int:pk>/', AccountDeleteView.as_view(), name='accounts_delete'),
    
]