from django.db.models.signals import post_save, pre_save
from django.dispatch import  receiver
from django.contrib.auth.models import User
from django.forms import ValidationError
from .models import Profile


@receiver(pre_save, sender=User)
def check_email(sender, instance, created,**kwargs):
    email = instance.email  
    if created:
        if sender.objects.filter(email=email).exclude(username=instance.username).exists():
            raise ValidationError('Email Already Exists')

    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            profile = instance.profile.exists()
        except Profile.DoesNotExist:
            profile = Profile(user=instance)
            profile.save()