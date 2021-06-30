from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from post.models import Post, Comment, Category
from .forms import CategoryForm, UserForm, UserUpdateForm, ProfileForm, PostForm
from .decorators import admin_and_editor_only, admin_only
from account.models import Profile

# Posts Views

@method_decorator(admin_and_editor_only, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'dashboard/post_list.html'
    context_object_name = 'posts'

@method_decorator(admin_and_editor_only, name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
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

@method_decorator(admin_and_editor_only, name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'dashboard/post_form.html'
    form_class = PostForm
    post_slug = None
    
    def test_func(self):
        return self.request.user.is_superuser or self.get_object().author == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, f'"{form.instance.title}" has been updated successfully')
        post = form.save()
        self.post_slug = post.slug
        return super().form_valid(form)    
    
        
    def get_success_url(self):
        return reverse('post:post', kwargs={'slug':self.post_slug})    

@method_decorator(admin_and_editor_only, name='dispatch')
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:posts')     
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f'"{self.get_object()}" has been deleted successfully')
        return super().delete(request, *args, **kwargs)
    
    
# Category Views 

@method_decorator(admin_and_editor_only, name='dispatch')
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'dashboard/category_list.html'
    context_object_name = 'categories'
    
@method_decorator(admin_and_editor_only, name='dispatch')
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dashboard/category_form.html'
    success_url = reverse_lazy('dashboard:categories')
    
    def form_valid(self, form):
        messages.success(self.request, f'"{form.instance.name}" has been created successfully')
        return super().form_valid(form)
    
@method_decorator(admin_and_editor_only, name='dispatch')
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    context_object_name = 'category'
    form_class = CategoryForm
    template_name = 'dashboard/category_form.html'
    success_url = reverse_lazy('dashboard:categories')
    
    
    def form_valid(self, form):
        messages.success(self.request, f'"{form.instance.name}" has been updated successfully')
        return super().form_valid(form)
        
@method_decorator(admin_and_editor_only, name='dispatch')    
class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:categories')     
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f'"{self.get_object()}" has been deleted successfully')
        return super().delete(request, *args, **kwargs)
    
# Comments Views

@method_decorator(admin_and_editor_only, name='dispatch')
class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'dashboard/comment_list.html'
    context_object_name = 'comments'
    

# Accounts Views
@method_decorator(admin_only, name='dispatch')
class AccountListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/account_list.html'
    context_object_name = 'accounts'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['editors_group'] = Group.objects.get(name='editors')
        except:
            Group.objects.create(name='editors')
        
        return context
        
@method_decorator(admin_only, name='dispatch')
class AccountCreateView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'dashboard/account_form.html'
    context_object_name = 'accounts'
    form_class = UserForm    
    success_url = reverse_lazy("dashboard:accounts")
    

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(self.request, f'"{form.instance.username}" has been created successfully')

        return super().form_valid(form)

@method_decorator(admin_only, name='dispatch')
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/account_form.html'
    context_object_name = 'account'
    form_class = UserUpdateForm    
    success_url = reverse_lazy("dashboard:accounts")    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['p_form'] = ProfileForm(instance=self.get_object())
            
        return context
    
    def post(self, request, *args, **kwargs):
        form_2 = ProfileForm(request.POST, request.FILES, instance=self.get_object())
        
        if form_2.is_valid():
            form_2.save()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        if form.is_valid():
            form.check_email(self.get_object().email)
            messages.success(self.request, f'"{form.instance.username}" has been updated successfully')
        return super().form_valid(form)    

@method_decorator(admin_only, name='dispatch')    
class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy("dashboard:accounts")        
    
    