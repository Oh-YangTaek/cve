from django.shortcuts import render
from search.models import CveTable
from django.http.response import HttpResponseRedirect, HttpResponse

from .forms import ProductForm,VersionForm

# Create your views here.

def Main(request):
    productForm = ProductForm()
    versionForm = VersionForm()
    return render(request, 'main.html',{'productForm':productForm,'versionForm':versionForm})

def ListFunc(request):
      if request.method == 'POST':
        productForm = ProductForm()
        versionForm = VersionForm()

        product = request.POST.get('product')
        version = request.POST.get('version')
        if product == '':
          datas = CveTable.objects.filter(product_version = version).order_by('id')
          return render(request, 'list.html',{'cve':datas,'productForm':productForm,'versionForm':versionForm})
        elif version == '':
          datas = CveTable.objects.filter(product = product).order_by('id')
          return render(request, 'list.html', {'cve':datas,'productForm':productForm,'versionForm':versionForm})
        else:
          datas = CveTable.objects.filter(product = product, product_version = version).order_by('id')
          return render(request, 'list.html', {'cve':datas,'productForm':productForm,'versionForm':versionForm})

