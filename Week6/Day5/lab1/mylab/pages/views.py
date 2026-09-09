from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    print(request)
    print(request.method)
    print(request.GET)
    print(request.path)

    return render(request, "home.html")



def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

def custom_404(request, exception):
    return render(request, "404.html", status=404)