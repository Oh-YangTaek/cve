from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(required = False, label = 'Product')
    product_version = forms.CharField(required = False, label = 'Product_version')

class ProductsForm(forms.Form):
    initial = forms.CharField(required = False)
