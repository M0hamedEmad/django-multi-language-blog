from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils.timezone import now
from django.db.models import Q
from .models import Category, Post
import random

class PostList(ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        # render posts that active = true and published_at before now
        queryset = self.model.objects.filter( Q(active=True) & Q(published_at__lte=now()) )
        return queryset
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        posts = self.model.objects.all()
        obj_categories = self.get_object().categories.all() # get object categories
        
        related_posts = None 
        if obj_categories: # Are object has category
            related_posts = posts.filter(categories__in=obj_categories)[:3]
        
        if related_posts is None:
            related_posts = random.sample(list(posts), 3)
        
        context['related_posts'] = related_posts
        
        return context