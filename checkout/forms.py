from django import forms
from .models import Order, ContactDetails


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2038)]

    credit_card_number = forms.CharField(
        label="Credit card number", required=False)
    cvv = forms.CharField(label="Security code (CVV)",
                          required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'full_name', 'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county', 'country')
        # next line found on StackOverflow:
        # https://stackoverflow.com/questions/15795869/django-modelform-to-have-a-hidden-input
        widgets = {'user': forms.HiddenInput}


class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ('user', 'full_name', 'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county', 'country')
        # next line found on StackOverflow:
        # https://stackoverflow.com/questions/15795869/django-modelform-to-have-a-hidden-input
        widgets = {'user': forms.HiddenInput}
