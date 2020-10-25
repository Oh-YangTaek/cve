from django import forms
from search.models import CveTable

class ProductForm(forms.Form):
    product = forms.CharField(required = False, label = 'Product')

class ProductVersionForm(forms.Form):
    product_version = forms.CharField(required = False, label = 'Product_version')

class SelectForm(forms.Form):
    select = forms.ChoiceField(required = False, choices=[(o['product'],o['product']) for o in  CveTable.objects.all().values('product').distinct().order_by('product')], label = 'Select')
