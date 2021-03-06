import random
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import now
from django.db.models import Q
from post.models import Post, Comment
from post.forms import CommentForm

class PostList(ListView):
    """ Home page """
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    def get_queryset(self):
        # render posts that active = true and published_at before now
        queryset = self.model.objects.filter( Q(active=True) & Q(published_at__lte=now()) )
        
        # filter posts by categories => if url path has a ?category=
        category = self.request.GET.get('category')
        
        
        if category:
            queryset = queryset.filter(categories__name=category)
            
        # Search Field
        qs = self.request.GET.get('q')
        
        if qs:
            qs = qs.strip()
            queryset = queryset.filter( Q(title__icontains=qs) | Q(content__icontains=qs) )
            
        return queryset
    
    
class PostDetail(FormMixin, DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'
    form_class = CommentForm
    
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
        return self.model.objects.filter( Q(active=True) & Q(published_at__lte=now()) )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        # related posts 

        posts = self.get_queryset()
        obj_categories = post.categories.all() # get object categories

        related_posts = None
        if obj_categories: # Are object has category
            related_posts = posts.filter(categories__in=obj_categories)[:3]

        # if related_posts none render 3 random posts
        if not related_posts:
            posts_list = list(posts)
            related_posts = random.sample(posts_list, min(len(posts_list), 3))

        context['related_posts'] = related_posts

        # comments
        comments = Comment.objects.filter( Q(post=post) & Q(active=True) )

        context['comments'] = comments

        context['comment_form'] = CommentForm

        return context
    
    
    def post(self, request, *args, **kwargs):
        self.obj = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
        
    def form_valid(self, form):
        form_2 = form.save(commit=False)
        form_2.user = self.request.user
        form_2.post = self.get_object()
        form_2.save()
        return super().form_valid(form)        
    
    def get_success_url(self):
        return reverse('post:post',  kwargs={'slug': self.get_object().slug})


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    
    def test_func(self):
        user = self.request.user
        return self.get_object().user == user or user.is_superuser or user.profile.is_admin
    
    def get_success_url(self):
        return reverse('post:post', kwargs={'slug':self.object.post.slug})
    