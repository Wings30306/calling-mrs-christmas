from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Cart(models.Model):
    """Save cart between sessions if user is logged in"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = JSONField(null=True, blank=True, default=dict)
