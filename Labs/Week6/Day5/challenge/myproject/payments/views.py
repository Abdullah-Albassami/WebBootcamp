from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def checkout(request):
    return render(request, "checkout.html")


def receipt(request):
    return render(request, "receipt.html")