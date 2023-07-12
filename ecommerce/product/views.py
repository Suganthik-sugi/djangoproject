from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import product
from .forms import UniversityForm
from .forms import UniversityForm1
from django import forms  
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.


def home(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        now = datetime.now()
        cdate = now.strftime('%d-%m-%Y')
        contact_data = product(productname=name, datecurrent=cdate)
    
        contact_data.save()
        return render(request, 'product/success.html')
    context={'form':UniversityForm}
    return render(request,'product/index2.html',context)


def forminsert(request):
      return render(request,'product/index.html')  
  
def result(request):
  mydata = product.objects.all()
  pro_dict={'pro_list':mydata}
  return render(request,'product/template.html',context=pro_dict)
#  return HttpResponse("Hello world!")

def update(request,id):
    if request.method=='POST':
        newproduct = product.objects.get(id=id)
        name = request.POST.get('ename')
        newproduct.productname=name
        newproduct.save()
        return redirect('result')
    
    return render(request, 'product/update.html', {'product': newproduct}) 

def delete(request,id):
    product_detail = product.objects.get(id=id)
    product_detail.delete()
    messages.error(request,"Delete Successfully completed")
    return redirect('result')
    # mydata = product.objects.all()
    # pro_dict={'pro_list':mydata}
    # return render(request,'product/template.html',context=pro_dict)

def edit(request,id):
     employee = product.objects.get(id=id) 
     pro_update={'product':employee,'form':UniversityForm1} 
     return render(request, 'product/update.html',context=pro_update)

def IntegrityError(request,exception):
    return render(request,'product/error.html')