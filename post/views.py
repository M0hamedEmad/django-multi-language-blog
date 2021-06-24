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
    paginate_by = 4
    
    def get_queryset(self):
        # render posts that active = true and published_at before now
        queryset = self.model.objects.filter( Q(active=True) & Q(published_at__lte=now()) )
        
        # filter posts by categories
        category = self.request.GET.get('category')
        
        if category:
            queryset = queryset.filter(categories__name=category)
            
        # Search Field
        q = self.request.GET.get('q')
        
        if q:
            q = q.strip()
            queryset = queryset.filter( Q(title__icontains=q) | Q(content__icontains=q) )
            
            
        return queryset
    
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'
    
    def get(self, request, *args, **kwargs):
        """ 
        overwrite get function to incrase views_count by 1 

        """
        post = self.get_object()
        post.views_count += 1
        post.save()
        return super().get(request,*args, **kwargs)
    
    def get_queryset(self):
        # render posts that active = true and published_at before now
        queryset = self.model.objects.filter( Q(active=True) & Q(published_at__lte=now()) )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        posts = self.get_queryset()
        obj_categories = self.get_object().categories.all() # get object categories
        
        related_posts = None 
        if obj_categories: # Are object has category
            related_posts = posts.filter(categories__in=obj_categories)[:3]
        
        # if related_posts none render 3 random posts
        if related_posts is None:
            related_posts = random.sample(list(posts), 3)
        
        context['related_posts'] = related_posts
        
        return context