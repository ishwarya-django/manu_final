from django import forms
from .models import Raw_material,Purchase_product
class Raw_material_Form(forms.ModelForm):
       class Meta:
        model = Raw_material
        fields = ('quantity', 'material','unit_price','measure')
class Purchase_product_form(forms.ModelForm):
       class Meta:
           model = Purchase_product
           fields = ['price_pro_fromshop']
