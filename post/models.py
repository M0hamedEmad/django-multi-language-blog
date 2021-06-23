from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

def upload_image(instance, image_name):
    """ Make a path to the post image and change the name of the image to a post id

    Returns:
        [str]: [image path]
    """
    _ , extension = image_name.split('.')
    return f"post_images/{instance.id}.{extension}"    
    


class Post(models.Model):
    active_field_choices = [
    (True, 'Active'),
    (False, 'Inactive')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(default='post_default_image.jpg', upload_to=upload_image, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    action = models.BooleanField(default=True, choices=active_field_choices)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
            Overwrite save mehtod to make a slug to post, rename a image and resize a big image
        """

        # Handle problem in upload_image function  (pk not generator yet)
        if self.pk is None:
            post_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = post_image

        # Make a post Slug
        self.slug = slugify(f"{self.title}-{self.id}")
            
        super().save(*args, **kwargs)
        
        # image resize
        img = Image.open(self.image.path)   
        if img.width > 800 or img.height > 800:
            img.thumbnail( (800, 800) )
            img.save(self.image.path)
            
        
