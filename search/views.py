from django.shortcuts import render
from search.models import CveTable
from django.http.response import HttpResponseRedirect
from .forms import SelectForm
from .forms import ProductForm
from .forms import ProductVersionForm

# Create your views here.

def Main(request):
    productForm = ProductForm()
    productVersionForm = ProductVersionForm()
    selectForm = SelectForm()
    return render(request, 'main.html',{'productForm':productForm,'productVersionForm':productVersionForm, 'selectForm':selectForm})

def ListFunc(request):
      if request.method == 'POST':
        productForm = ProductForm()
        productVersionForm = ProductVersionForm()
        selectForm = SelectForm()
        product = request.POST.get('product')
        product_version = request.POST.get('product_version')
        select = request.POST.get('select')
        if select != '':
          datas = datas = CveTable.objects.filter(product = select).order_by('id')
          return render(request, 'list.html', {'cve':datas,'productForm':productForm,'productVersionForm':productVersionForm, 'selectForm':selectForm})
        elif product == '':
          datas = CveTable.objects.filter(product_version = product_version).order_by('id')
          return render(request, 'list.html',{'cve':datas,'productForm':productForm,'productVersionForm':productVersionForm, 'selectForm':selectForm})
        elif product_version == '':
          datas = CveTable.objects.filter(product = product).order_by('id')
          return render(request, 'list.html', {'cve':datas,'productForm':productForm,'productVersionForm':productVersionForm, 'selectForm':selectForm})
        else:
          datas = CveTable.objects.filter(product = product, product_version = product_version).order_by('id')
          return render(request, 'list.html', {'cve':datas,'productForm':productForm,'productVersionForm':productVersionForm, 'selectForm':selectForm})

def test(request):
      if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
           pass
      elif request.method == 'GET':
        form = SearchForm()
        return render(request,'test.html',{'form':form})
      else:
        pass
def test2(request):
      return render(request,'test2.html')
