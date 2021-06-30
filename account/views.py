from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import FormView, View
from .forms import UserLoginForm,RegistrationForm


class RegisterView(FormView):
    model = User
    template_name = 'account/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('post:home')
    
    def get(self, *args, **kwargs):
        """ 
        check if user already login redierct to home page
        """
        if self.request.user.is_authenticated:
            return redirect('post:home')
        return super().get(*args, **kwargs)

    
    def form_valid(self, form):
        """ 
        override form_vaild finction to make user login after register
        Note:
            if you add email verification delete it    
            
        """
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    

class LoginPage(LoginView):
    template_name = 'account/login.html'
    form_class = UserLoginForm
    
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
    
class LogoutPage(LogoutView):
    next_page = reverse_lazy('post:home')

    # def get_next_page(self):
    #     messages.success(self.request, 'You have successfully logged out')
    #     super().get_next_page()
    
class ProfileView(View):
    def get(self, request, *argks, **kwargs):
        return render(request, 'account/profile.html')