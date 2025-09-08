from django import forms
from .models import ProductInquiry

class ProductInquiryForm(forms.ModelForm):
    class Meta:
        model = ProductInquiry
        fields = ['name', 'email','phone', 'message']