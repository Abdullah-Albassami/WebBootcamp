from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_view(request):
    return HttpResponse("CREATE VIEW")


def details_view(request, id):
    return HttpResponse(f"DETAIL VIEW - Product ID: {id}")
