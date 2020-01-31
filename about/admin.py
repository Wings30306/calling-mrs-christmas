from django.contrib import admin

# Register your models here.
from .models import Employee, CaseStudy


admin.site.register(Employee)
admin.site.register(CaseStudy)