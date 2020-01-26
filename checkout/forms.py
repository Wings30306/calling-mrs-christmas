from django import forms
from .models import Order, ContactDetails


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2038)]

    credit_card_number = forms.CharField(
        label="Credit card number",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "aria-label": "Credit card number",
            "placeholder": "Credit card number"
        }))
    cvv = forms.CharField(label="Security code (CVV)",
                          required=False,
                          widget=forms.TextInput(attrs={
                              "class": "form-control",
                              "aria-label": "CVV",
                              "placeholder": "CVV",
                              "max-length": 5
                          }))
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput())


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'full_name', 'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county', 'country')
        # HiddenInput found on StackOverflow:
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
