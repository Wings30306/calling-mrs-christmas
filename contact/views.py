from django.shortcuts import render, redirect, reverse
from .models import Location
from .forms import ContactForm

# Create your views here.


def contact_view(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
        return redirect(reverse('accounts:profile'))
    else:
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
