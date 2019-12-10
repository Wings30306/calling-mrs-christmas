from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Employee, CaseStudy

# Create your views here.
def index_view(request):
    template_name = "main.html"
    queryset = CaseStudy.objects.all()
    context = {
        "queryset": queryset
    }
    return render(request, template_name, context)

def about_view(request):
    template_name = "about.html"
    object_list = User.objects.filter(is_staff=True)
    context = {
        "object_list": object_list
        }
    return render(request, template_name, context)

def detail_view(request, user):
    template_name = "staffmember.html"
    try:
        obj = User.objects.get(username=user)
        print(obj)
        if obj.is_staff:
            context = {
                "obj": obj
            }
        else:
            messages.error(request, 'No staff member with this username')
            return redirect("about:about_list")
    except User.DoesNotExist:
        messages.error(request, 'No staff member with the username <em>' + user + '<em>.')
        return redirect("about:about_list")
    return render(request, template_name, context)
    