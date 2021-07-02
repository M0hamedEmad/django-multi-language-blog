from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from dashboard.decorators import get_or_create_editor_admin_group
from PIL import Image

def upload_image(instance, image_name):
    """ Make a path to the post image and change the name of the image to a post id

    Returns:
        [str]: [image path]
    """
    _ , extension = image_name.split('.')
    return f"profile_pics/{instance.id}.{extension}"    
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    picture = models.ImageField(_('image'), default='profile_pics/default.jpg', upload_to=upload_image, null=True, blank=True)
    
    @property    
    def is_admin(self):        
        _ , admin_group = get_or_create_editor_admin_group()
        
        if self.user.is_superuser:
            return True

        elif self.user.groups.exists():
            if admin_group in self.user.groups.all():
                return True

        return False
    
    @property    
    def is_admin_or_editor(self):        
        editors_group , admin_group = get_or_create_editor_admin_group()
        
        if self.user.is_superuser:
            return True

        elif self.user.groups.exists():
            groups = self.user.groups.all()
            if admin_group in groups or editors_group in groups:
                return True

        return False
        
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
            
        