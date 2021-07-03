from django import forms
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from post.models import Post, Comment, Category, PostLanguage
from account.models import Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'categories', 'image', 'language', 'active', 'published_at',)       
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs = {
            'placeholder':_('Write your title here')
        }
        
        self.fields['content'].widget.attrs = {
            'placeholder':_('Write content here')
        }

class PostLanguageForm(forms.ModelForm):
    class Meta:
        model = PostLanguage
        fields = ('title', 'content', 'categories', 'active', 'post', 'language')       
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs = {
            'placeholder':_('Write your title here')
        }
        
        self.fields['content'].widget.attrs = {
            'placeholder':_('Write content here')
        }         
            
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )
        
class UserForm(forms.ModelForm):
    username = forms.CharField(label=_('username'), help_text='', max_length=70)
    password = forms.CharField(label=_('Password'), min_length=8, max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('Confirm Password'), min_length=8, max_length=50, widget=forms.PasswordInput())
    email = forms.EmailField(label=_('Email'), required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2','groups', 'is_staff', 'is_active')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('The two password fields didn’t match.')
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')
        return email  
    
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label=_('username'), help_text='', max_length=70)
    email = forms.EmailField(label=_('Email'), required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'groups', 'is_staff', 'is_active')
        
    def check_email(self, e_mail):
        email = self.cleaned_data.get('email')
        if email == e_mail:
            return self.cleaned_data
        if User.objects.filter(email=email).exists():
            self.clean_email(is_clean=False)
        return email      
    
    def clean_email(self, is_clean=True):
        if is_clean:
            return self.cleaned_data.get('email')
        else:
            raise forms.ValidationError('Email already exists.')
 
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', )        