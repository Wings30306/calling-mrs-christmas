from django.db import models
from django.core.files.storage import default_storage as storage
from PIL import Image, ImageOps

# Create your models here.
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    intro = models.TextField()
    profile_pic = models.ImageField()
    is_staff = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        - installed 'django-cleanup' to auto-remove old image.
        - installed 'pillow' to resize larger images.
        - resizes all image formats except '.gif' as these cannot be resized
        """
        super(Employee, self).save(*args, **kwargs)
        if self.profile_pic:
            extension = "png"
            img = Image.open(self.profile_pic)
            new = ImageOps.fit(img, (500, 500))
            temp = storage.open(self.profile_pic.name, "w")
            new.save(temp.name, extension)
            temp.close()
            # continue if image format is not .gif
            super(Employee, self).save(*args, **kwargs)

    