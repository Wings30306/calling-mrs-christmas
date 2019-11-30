from django.db import models
from django.core.files.storage import default_storage as storage

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    brief_description = models.TextField()
    detailed_description = models.TextField()
    image = models.ImageField()
    image_description = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=9, default=4.99)
    available = models.BooleanField(default=True)