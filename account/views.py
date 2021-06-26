from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserLoginForm

class LoginPage(LoginView):
    template_name = 'account/login.html'
    form_class = UserLoginForm
    # authentication_form = UserLoginForm
    
    def get(self, request, *args, **kwargs):
        """ 
        check if user already login redierct to home page
        if user redierict from some place in site render login page in massage
        """
        if request.user.is_authenticated:
            if '?next=/' in request.get_full_path():
                return super().get(request, *args, **kwargs)
            else:
                return redirect('post:home')
        
        return super().get(request, *args, **kwargs)
    

class RegisterView(CreateView):
    model = User
    template_name = 'account/register.html'
    

