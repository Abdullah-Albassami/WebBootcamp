from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home</h1> <p> Welcome to Home Page</p>")


def about(request):
    return HttpResponse("<h1>About</h1> <p> Welcome to About Page</p>")


def contact(request):
    return HttpResponse("<h1>Contact</h1> <p> Welcome to Contact Page</p>")
