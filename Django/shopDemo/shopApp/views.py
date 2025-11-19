from django.shortcuts import render,redirect
from .models import Customers
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
    
    
def shop(request):
    return render(request,'shop.html')

def why(request):
    return render(request,'why.html')

def contact(request):
    return render(request,'contact.html')

def regis(request):
    return render(request,'regis.html')

def testimonial(request):
    return render(request,'testimonial.html')

def userdtl(request):
    return render(request,'userdtl.html')