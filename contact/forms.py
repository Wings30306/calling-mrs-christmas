from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            "user", "name", "email", "message"
        ]
        widgets = {"user": forms.HiddenInput()}
