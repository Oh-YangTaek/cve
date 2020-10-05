from django.shortcuts import render
from search.models import CveTable
from django.http.response import HttpResponseRedirect
from .forms import SearchForm

# Create your views here.

def Main(request):
    form = SearchForm()
    return render(request, 'main.html',{'form':form})

def ListFunc(request):
      if request.method == 'POST':
        form = SearchForm()
        product = request.POST.get('product')
        product_version = request.POST.get('product_version')
        datas = CveTable.objects.filter(product=product,product_version = product_version).order_by('id')
        return render(request, 'list.html' ,{'cve':datas,'form':form})

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
