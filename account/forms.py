from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class UserLoginForm(AuthenticationForm):
    # username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)

    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            User.objects.get
            
            user = authenticate(username=username, password=password)

            if user.is_active:
                raise forms.ValidationError('This user is not active')
            if user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user:
                raise forms.ValidationError('This user does not exist')
            
        return super().clean(*args, **kwargs)