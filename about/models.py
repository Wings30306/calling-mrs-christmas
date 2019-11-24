from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    intro = models.TextField()
    profile_pic = models.ImageField()
    is_staff = models.BooleanField(default=True)