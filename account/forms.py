from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email or Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
