from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("index")

def faq(request):
    return HttpResponse("faq")

def team(request):
    return HttpResponse("team")
