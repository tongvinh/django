from django import forms
from .models import ContactForm


class Contact_Form(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)
