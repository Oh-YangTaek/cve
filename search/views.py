from django.shortcuts import render
from search.models import CveTable
from django.http.response import HttpResponseRedirect
from .forms import SearchForm
from .forms import ProductsForm

# Create your views here.

def Main(request):
    form = SearchForm()
    initial = ProductsForm
    return render(request, 'main.html',{'form':form, 'initial':initial})

def ListFunc(request):
      if request.method == 'POST':
        form = SearchForm()
        product = request.POST.get('product')
        product_version = request.POST.get('product_version')
        if product == '':
          datas = CveTable.objects.filter(product_version = product_version).order_by('id')
          return render(request, 'list.html',{'cve':datas,'form':form})
        elif product_version == '':
          datas = CveTable.objects.filter(product = product).order_by('id')
          return render(request, 'list.html', {'cve':datas,'form':form})
        else:
          datas = CveTable.objects.filter(product = product, product_version = product_version).order_by('id')
          return render(request, 'list.html', {'cve':datas,'form':form})

def Products(request):
      if request.method == 'POST':
        initial = request.POST.get('initial')
        datas = CveTable.objects.filter(product__(i)startswith = initial).distinct('product')
        return render(request,'products.html',{'cve':datas})

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
