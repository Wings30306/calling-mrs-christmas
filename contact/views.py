from django.shortcuts import render

# Create your views here.
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html")