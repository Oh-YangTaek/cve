from django import forms
from search.models import CveTable

class ProductForm(forms.Form):
    product = forms.ChoiceField(initial = '--------------------', required = False, choices=[(o['product'],o['product']) for o in  CveTable.objects.all().values('product').distinct().order_by('product')], label = 'Product')
class VersionForm(forms.Form):
    version = forms.ChoiceField(initial = '--------------------', required = False, choices=[(o['product_version'],o['product_version']) for o in  CveTable.objects.all().values('product_version').distinct().order_by('product_version')], label = 'Version')
