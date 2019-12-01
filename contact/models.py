from django.db import models

# Create your models here.
class Location(models.Model):
    street = models.CharField(max_length=100, default="High Street")
    number = models.DecimalField(max_digits=5, decimal_places=0, default="120")
    postcode = models.CharField(max_length=12, default="HP1 3AR")
    town = models.CharField(max_length=100, default="Hemel Hempstead")
    latitude = models.DecimalField(max_digits=10, decimal_places=6, default=51.753658)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, default=-0.474900)
    email = models.EmailField(default="info@callingmrschristmas.com")
    image = models.ImageField()
