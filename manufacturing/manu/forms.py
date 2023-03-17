from dataclasses import fields
from django import forms
from .models import Manufacturing,Product,SellProduct






class ChargeForm(forms.ModelForm):
    class Meta:
        model=Manufacturing
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['manufactured_product','manufactured_quantity','measure']

class SoldForm(forms.ModelForm):
    class Meta:
        model=SellProduct
        fields=['sell_quantity','quantity_price','product_name','customer']

class ByProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['manufactured_product','manufactured_quantity','measure','purchase_price']