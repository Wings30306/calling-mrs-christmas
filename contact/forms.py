from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            "user", "name", "email", "message"
        ]
        widgets = {"user": forms.HiddenInput(),
                   "name": forms.TextInput(attrs={
                       "class": "form-control"
                   }),
                   "email": forms.EmailInput(attrs={
                       "class": "form-control"
                   }),
                   "message": forms.Textarea(attrs={
                       "class": "form-control",
                       "rows": 10,
                   })
                   }
