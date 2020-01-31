from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactDetails


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""
    username = forms.CharField(label='Your name',
                               max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'}))


class UserRegistrationForm(UserCreationForm):
    """Form to be used to register a new user"""
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a password'}),
    )
    password2 = forms.CharField(label="Password Confirmation",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Confirm your password'},
                                    render_value=True))

    class Meta:
        widgets = {
            "username": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Choose a username'
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your email'
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your first name'
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your last name'
                }
            )}
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password")
        if password2 != password1:
            raise forms.ValidationError("Passwords must match")
        return password2

class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ('user', 'full_name', 'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county', 'country')
        # next line found on StackOverflow:
        # https://stackoverflow.com/questions/15795869/django-modelform-to-have-a-hidden-input
        widgets = {'user': forms.HiddenInput(),
                   'full_name': forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Your name",
                       "placeholder": "Your name"
                   }),
                   "phone_number": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Your phone number",
                       "placeholder": "Your phone number"
                   }),
                   "street_address1": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Address line 1",
                       "placeholder": "Address line 1"
                   }),
                   "street_address2": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Address line 2",
                       "placeholder": "Address line 2"
                   }),
                   "town_or_city": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Town or city",
                       "placeholder": "Town or city"
                   }),
                   "postcode": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Postcode",
                       "placeholder": "Postcode"
                   }),
                   "county": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "County",
                       "placeholder": "County"
                   }),
                   "country": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Country",
                       "placeholder": "Country",
                       "default": "United Kingdom"
                   }),
                   }
