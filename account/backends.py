from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import  Q
from django import forms

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            )
        
        except User.DoesNotExist:
            raise forms.ValidationError("This user does not exist")
        
        except MultipleEmailBackend:
            return user.order_by('id').first()
        
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            
            elif not user.check_password(password):
                raise forms.ValidationError("Your username and password didn't match. Please try again")

            elif not user.is_active:
                raise forms.ValidationError("This user is not active")
            
            else:
                raise forms.ValidationError("Login error. Please try again. If this problem persists, contact the site admin")
            
        def get_user(self, user_id):
            try:
                user = User.objects.get(pk=user_id)
                
            except User.DoesNotExist:
                return None
            
            return user if self.user_can_authenticate(user) else None