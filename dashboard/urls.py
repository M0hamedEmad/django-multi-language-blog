from django.urls import path
from  .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostLanguageListView,
    PostLanguageCreateView,
    PostLanguageUpdateView,
    PostLanguageDeleteView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CommentListView,
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    LanguageListView,
    LanguageCreateView,
    LanguageUpdateView,
    LanguageDeleteView,
    )

app_name = 'dashboard'

urlpatterns = [
    # Post Urls
    path('dashboard/', PostListView.as_view(), name='dashboard'),
    
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    
    path('posts/translation/', PostLanguageListView.as_view(), name='posts_language'),
    path('post/add/translation/<int:id>/', PostLanguageCreateView.as_view(), name='post_language_create'),
    path('post/update/translation/<int:pk>/', PostLanguageUpdateView.as_view(), name='post_language_update'),
    path('post/delete/translation/<int:pk>/', PostLanguageDeleteView.as_view(), name='post_language_delete'),
    
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
        
    # Language Urls
    path('languages/', LanguageListView.as_view(), name='languages'),
    path('languages/create/', LanguageCreateView.as_view(), name='create_language'),
    path('languages/update/<int:pk>/', LanguageUpdateView.as_view(), name='update_language'),
    path('languages/delete/<int:pk>/', LanguageDeleteView.as_view(), name='delete_language'),
    
]