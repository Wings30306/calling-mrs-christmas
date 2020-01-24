from django.shortcuts import render, redirect
from .models import Location, ContactMessage
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    context = {
        "form": ContactForm(),
        "locations": Location.objects.all()
    }
    return render(request, "contact.html", context=context)
