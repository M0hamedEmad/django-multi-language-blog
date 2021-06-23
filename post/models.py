from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

def upload_image(instance, image_name):
    _ , extension = image_name.split('.')
    return f"post_images/{instance.id}.{extension}"

class Post(models.Model):
    active_field_choices = [
    (True, 'ِctive'),
    (False, 'Inactive')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    categories = models.ManyToManyField('category')
    image = models.ImageField(default='post_default_image.jpg', upload_to='upload_image')
    slug = models.SlugField()
    action = models.BooleanField(default=True, choices=active_field_choices)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    