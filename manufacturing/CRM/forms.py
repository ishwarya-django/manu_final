from django import forms
from .models import Customer
class Customer_Form(forms.ModelForm):
       class Meta:
        model = Customer
        fields = ('name', 'phone_number','email','place','district','state','country','pincode','organization')
