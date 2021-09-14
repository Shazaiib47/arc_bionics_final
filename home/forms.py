from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """contact form will be here"""
    class Meta:
        model = Contact

        fields = "__all__"
