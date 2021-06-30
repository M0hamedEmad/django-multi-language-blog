from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def upload_image(instance, image_name):
    """ Make a path to the post image and change the name of the image to a post id

    Returns:
        [str]: [image path]
    """
    _ , extension = image_name.split('.')
    return f"profile_pics/{instance.id}.{extension}"    
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='profile_pics/default.jpg', upload_to=upload_image, null=True, blank=True)
    
    def __str__(self):
        try:
            return self.user.username
        except:
            return "none"
    
    def save(self, *args, **kwargs):
        """
            Overwrite save mehtod to rename a image and resize a big image
        """

        # Handle problem in upload_image function  (pk not generator yet)
        if self.pk is None:
            image = self.picture
            self.picture = None
            super().save(*args, **kwargs)
            self.picture = image

        super().save(*args, **kwargs)
        
        # image resize
        img = Image.open(self.picture.path)   
        if img.width > 400 or img.height > 400:
            img.thumbnail( (400, 400) )
            img.save(self.picture.path)
            
        