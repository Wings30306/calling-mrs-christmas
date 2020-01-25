from django.shortcuts import render, redirect
from .models import Location, ContactMessage
from .forms import ContactForm

# Create your views here.


def contact_view(request):
    if request.user.is_authenticated:
        initial_data = {
            "user": request.user,
            "name": request.user.first_name + " " + request.user.last_name,
            "email": request.user.email
        }
        form = ContactForm(
            request.POST or None, initial=initial_data)
    else:
        form = ContactForm()

    context = {
        "form": form,
        "locations": Location.objects.all()
    }
    return render(request, "contact.html", context=context)
