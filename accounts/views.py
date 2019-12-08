from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.
def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('index'))

def register(request):
    """Allow new user to create account"""
    auth.logout(request)
    return redirect(reverse('index'))

def login(request):
    """Log the user in to their account"""
    auth.logout(request)
    return redirect(reverse('index'))

def profile(request):
    """Redirect user to their profile"""
    auth.logout(request)
    return redirect(reverse('index'))

def edit_profile(request):
    """Allow user to edit their profile info"""
    auth.logout(request)
    return redirect(reverse('index'))