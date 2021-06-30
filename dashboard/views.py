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