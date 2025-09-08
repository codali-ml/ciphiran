from django.forms import ModelForm
from django import forms
from .models import Contact ,Careers


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','body']


class CareerForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = ['name', 'email', 'phone', 'position', 'resume', 'employment_type', 'location']
        widgets = {"resume": forms.ClearableFileInput(attrs={"id": "resume"})}

