from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Employee

# Create your views here.
def index_view(request):
    template_name = "main.html"
    return render(request, template_name)

def about_view(request):
    template_name = "about.html"
    object_list = User.objects.all()
    context = {
        "object_list": object_list
        }
    return render(request, template_name, context)

def detail_view(request, id):
    template_name = "staffmember.html"
    obj = get_object_or_404(User, id=id)
    if obj.employee.is_staff == True:
        print(obj.employee.profile_pic)
        context = {
            "obj": obj
        }
    else:
        messages.error(request, 'No staff member matching this id')
        return redirect(about_view)
    return render(request, template_name, context)
    