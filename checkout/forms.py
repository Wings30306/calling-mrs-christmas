from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2038)]

    credit_card_number = forms.CharField(max_length=16, min_length=16,
                                         label="Credit card number")
    cvv = forms.CharField(max_length=3, min_length=3,
                          label="Security code (CVV)")
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'country', 'postcode', 'country')
