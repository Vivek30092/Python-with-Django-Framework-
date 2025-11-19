from django.shortcuts import render
from django.http import HttpResponse
from demoapp.models import Registration
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def disp(request):
    s = "<h1> This is my first djanog view</h1>"
    return HttpResponse(s)

def temp(request)

def regdata(request)
