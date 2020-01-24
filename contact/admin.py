from django.contrib import admin

# Register your models here.
from .models import Location, ContactMessage

admin.site.register(Location)
admin.site.register(ContactMessage)
