from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("<h1>Welcome To The Home Page!</h1>")
