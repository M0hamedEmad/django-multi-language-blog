from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib import messages
from post.models import Post, Comment, Category
from account.models import Profile
from .forms import CategoryForm, UserForm, UserUpdateForm, ProfileForm, PostForm

# Posts Views

class PostListView(ListView):
    model = Post
    template_name = 'dashboard/post_list.html'
    context_object_name = 'posts'
    

class PostCreateView(CreateView):
    model = Post
    template_name = 'dashboard/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('dashboard:posts')
    post_slug = None

    def form_valid(self, form):
        form_2 = form.save(commit=False)
        form_2.author = self.request.user
        form_2.save()
        self.post_slug = form_2.slug
        messages.success(self.request, f'"{form.instance.title}" has been created successfully')
            
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post:post', kwargs={'slug':self.post_slug})

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'dashboard/post_form.html'
    form_class = PostForm
    post_slug = None
    
    def form_valid(self, form):
        messages.success(self.request, f'"{form.instance.title}" has been updated successfully')
        post = form.save()
        self.post_slug = post.slug
        return super().form_valid(form)    
    
        
    def get_success_url(self):
        return reverse('post:post', kwargs={'slug':self.post_slug})    


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:posts')     
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f'"{self.get_object()}" has been deleted successfully')
        return super().delete(request, *args, **kwargs)
        