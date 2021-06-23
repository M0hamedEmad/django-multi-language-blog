from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Post

class PostList(ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'