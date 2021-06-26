from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm

class LoginPage(LoginView):
    template_name = 'account/login.html'
    # form_class = UserLoginForm
    authentication_form = UserLoginForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if '?next=/' in request.get_full_path():
                return super().get(request, *args, **kwargs)
            else:
                return redirect('post:home')
        
        return super().get(request, *args, **kwargs)
