from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CaseStudy

# Create your views here.
def index_view(request):
    """ Render index page with case study as success story """
    template_name = "main.html"
    queryset = CaseStudy.objects.all()
    context = {
        "queryset": queryset
    }
    return render(request, template_name, context)

def about_view(request):
    """ Render About Us page with a list of staff members """
    template_name = "about.html"
    object_list = User.objects.filter(is_staff=True)
    context = {
        "object_list": object_list
        }
    return render(request, template_name, context)

def detail_view(request, user):
    """ Render profile page for staff member.
    If no staff member by that username, return user to About page,
    show user an error message "no staff member with this username". """
    template_name = "staffmember.html"
    try:
        obj = User.objects.get(username=user)
        print(obj)
        if obj.is_staff:
            context = {
                "obj": obj
            }
        else:
            messages.error(request, 'No staff member with the username <em>' + user + '</em>.')
            return redirect("about:about_list")
    except User.DoesNotExist:
        messages.error(request, 'No staff member with the username <em>' + user + '</em>.')
        return redirect("about:about_list")
    return render(request, template_name, context)
