from django.contrib import admin

# Register your models here.
from .models import Service, ServiceCategory

admin.site.register(Service)
admin.site.register(ServiceCategory)