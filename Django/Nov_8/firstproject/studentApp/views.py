from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dis(request):
    s = "<h1>this is my first web response </h1>"
    return HttpResponse(s)