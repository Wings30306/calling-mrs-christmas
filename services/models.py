from django.db import models
from django.urls import reverse

# Create your models here.


class ServiceCategory(models.Model):
    """"Model to store service categories (comparable to product types in a webshop)"""
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    description = models.TextField()
    name = models.CharField(max_length=100, unique=True)
    img_alt = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Get absolute url for an instance of this model"""
        return reverse("services:services_list_by_cat", kwargs={"category": self.name})


class Service(models.Model):
    """Get absolute url for a service's detail page"""
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    category = models.ForeignKey(
        ServiceCategory, related_name='services', on_delete=models.CASCADE)
    brief_description = models.TextField()
    detailed_description = models.TextField()
    img_name = models.CharField(max_length=100)
    img_alt = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=9, default=4.99)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Get absolute url for an instance of this model"""
        return reverse("services:service_detail", kwargs={"primary_key": self.id})
