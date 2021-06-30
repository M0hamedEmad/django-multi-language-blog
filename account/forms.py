from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email or Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(help_text='', label='Username')
    email = forms.CharField(help_text='', label="Email", widget=forms.EmailInput())
    password1 = forms.CharField(help_text='', label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(help_text='', label="Password confirmation:", widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email aleardy exists')
        
        return email
        