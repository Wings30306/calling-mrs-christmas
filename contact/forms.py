from django import forms

from .models import Location


class LocationModelForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'number',
            'street',
            'town',
            'postcode',
            'email',
        ]
