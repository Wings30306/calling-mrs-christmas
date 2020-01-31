from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """ Form for the input of contact messages """
    class Meta:
        model = ContactMessage
        fields = [
            "user", "name", "email", "message"
        ]
        widgets = {"user": forms.HiddenInput(),
                   "name": forms.TextInput(attrs={
                       "class": "form-control",
                       "aria-label": "Your name",
                       "placeholder": "Your name"
                   }),
                   "email": forms.EmailInput(attrs={
                       "class": "form-control",
                       "aria-label": "Your email",
                       "placeholder": "Your email"
                   }),
                   "message": forms.Textarea(attrs={
                       "class": "form-control",
                       "rows": 10,
                       "aria-label": "Your message",
                       "placeholder": "Your message"
                   })
                   }
