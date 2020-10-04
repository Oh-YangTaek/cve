from django import forms


class SearchForm(forms.Form):
    platform = forms.CharField(label = 'Product')
    platform_version = forms.CharField(label = 'Product_version')
