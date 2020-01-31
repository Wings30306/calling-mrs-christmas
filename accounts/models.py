from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return str(self.user) + " - " + self.full_name
