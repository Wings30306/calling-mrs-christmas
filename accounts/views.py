from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from checkout.models import Order
from .forms import UserLoginForm, UserRegistrationForm, ContactDetailsForm
from .models import ContactDetails


# Create your views here.


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "Thanks for visiting, see you again soon!")
    return redirect(reverse('index'))


def register(request):
    """Allow new user to create account"""
    if request.user.is_authenticated:
        # Prevent logged in user from going back to login page
        messages.success(request, request.user.first_name +
                         ", you are already signed in!")
        return redirect(reverse('index'))
    if request.method == "POST":
        # Register the user using form data
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome, " + user.first_name +
                                 "! Your account was successfully created.")
                return redirect(reverse('accounts:profile'))
            else:
                registration_form.add_error(
                    request("Sorry, we are unable to register your account at this time."))

    else:
        registration_form = UserRegistrationForm
    context = {
        "form": registration_form,
        "form_title_upper": "Create a new account",
        "form_title_lower": "Register now!",
        "button_text": "Create account",
        "wrong_page_redirect": "<p>Do you already have an account? " +
                               "You can <a href='/accounts/login'>sign in</a> instead.</p>"
    }
    return render(request, "form.html", context)


def login(request):
    """Return Login page"""
    if request.user.is_authenticated:
        # Prevent logged in user from going back to login page
        messages.success(request, request.user.first_name +
                         ", you are already signed in!")
        return redirect(reverse('accounts:profile'))
    if request.method == "POST":
        # Log in the user using form data
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome, " + user.first_name + "!")
                return redirect(reverse('accounts:profile'))
            else:
                form.add_error(None, "Your username or password is incorrect.")
    else:
        form = UserLoginForm
    context = {
        "form": form,
        "form_title_upper": "Welcome back!",
        "form_title_lower": "Please log in",
        "button_text": "Log me in",
        "wrong_page_redirect": "<p><strong>If you were redirected here after password reset, " +
                               "please sign in again with your new password.</strong></p>" +
                               "<p>If you forgot your password, you can " +
                               "<a href='password-reset'>reset</a> it.</p>" +
                               "<p>You don't have an account yet? " +
                               "You can <a href='register'>sign up</a> instead.</p>"
    }
    return render(request, "form.html", context)


@login_required
def user_profile(request):
    """Render user's profile page"""
    if request.method == "POST":
        contact_details_form = ContactDetailsForm(request.POST)
        form_dict = contact_details_form.__dict__
        full_name = form_dict["data"]["full_name"]
        phone = form_dict["data"]["phone_number"]
        street1 = form_dict["data"]["street_address1"]
        street2 = form_dict["data"]["street_address2"]
        town = form_dict["data"]["town_or_city"]
        postcode = form_dict["data"]["postcode"]
        county = form_dict["data"]["county"]
        country = form_dict["data"]["country"]
        try:
            ContactDetails.objects.get(user=request.user)
            ContactDetails.objects.filter(user=request.user).update(
                user=request.user,
                full_name=full_name,
                phone_number=phone,
                street_address1=street1,
                street_address2=street2,
                town_or_city=town,
                postcode=postcode,
                county=county,
                country=country)
            print("updating instance")
        except ContactDetails.DoesNotExist:
            print("creating instance")
            ContactDetails.objects.create(
                user=request.user,
                full_name=full_name,
                phone_number=phone,
                street_address1=street1,
                street_address2=street2,
                town_or_city=town,
                postcode=postcode,
                county=county,
                country=country)
            print(ContactDetails.objects.get(user=request.user))
        messages.success(
            request, "Your contact details have been updated, " + request.user.first_name + ".")
        return redirect(reverse("accounts:profile"))
    else:
        user = User.objects.get(username=request.user.username)
        try:
            ContactDetails.objects.get(user=request.user)
            contact_data = {
                "user": request.user.id,
                "full_name": request.user.contactdetails.full_name,
                "phone_number": request.user.contactdetails.phone_number,
                "street_address1": request.user.contactdetails.street_address1,
                "street_address2": request.user.contactdetails.street_address2,
                "town_or_city": request.user.contactdetails.town_or_city,
                "postcode": request.user.contactdetails.postcode,
                "county": request.user.contactdetails.county,
                "country": request.user.contactdetails.country
            }
        except ContactDetails.DoesNotExist:
            contact_data = {
                "full_name": request.user.first_name + " " + request.user.last_name,
            }
        contact_details = ContactDetailsForm(
            request.POST or None, initial=contact_data)
        purchases = Order.objects.filter(user=request.user)
        context = {
            "profile": user,
            "contact_details_form": contact_details,
            "purchases": purchases
        }
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    """Allow user to edit their profile info"""
    form = UserRegistrationForm
    context = {
        "form": form,
        "form_title": "Edit my profile",
        "button_text": "Save"
    }
    return render(request, "form.html", context)
