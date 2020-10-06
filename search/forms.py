from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(label = 'Product')
    product_version = forms.CharField(label = 'Product_version')
