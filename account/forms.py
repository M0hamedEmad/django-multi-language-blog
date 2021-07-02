from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Email or Username')}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':_('Password')}))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(help_text='', label=_('Username'))
    email = forms.CharField(help_text='', label=_('Email'), widget=forms.EmailInput())
    password1 = forms.CharField(help_text='', label=_('Password'), widget=forms.PasswordInput())
    password2 = forms.CharField(help_text='', label=_('Password confirmation'), widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email aleardy exists')
        
        return email
       
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        user = User.objects.get(username=username)
        
        if User.objects.filter(email=email).count() > 1:
            raise forms.ValidationError('Email already exists.')        
   
        return email      
    
                