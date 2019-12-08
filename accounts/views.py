from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "Thanks for visiting, see you again soon!")
    return redirect(reverse('index'))

def register(request):
    """Allow new user to create account"""
    auth.logout(request)
    return redirect(reverse('index'))

def login(request):
    ""

    """Log the user in to their account"""
    if request.method == POST:
        return redirect(reverse('index'))

def profile(request, username):
    """Redirect user to their profile"""
    
    return redirect(reverse('index'))

def edit_profile(request, username):
    """Allow user to edit their profile info"""
    return redirect(reverse('index'))