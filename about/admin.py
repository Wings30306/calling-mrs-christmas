from django.contrib import admin

# Register your models here.
from .models import Employee, CaseStudy 
# , CaseStudyImage


admin.site.register(Employee)
admin.site.register(CaseStudy)
# admin.site.register(CaseStudyImage)