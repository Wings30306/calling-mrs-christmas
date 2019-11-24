from django.shortcuts import render
from django.contrib.auth.models import User

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