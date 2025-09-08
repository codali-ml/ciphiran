from django import forms
from .models import ServiceInquiry

class ServiceInquiryForm(forms.ModelForm):
    class Meta:
        model = ServiceInquiry
        fields = ['name', 'email','phone', 'message']