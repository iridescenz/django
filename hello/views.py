from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def irina(request):
    return HttpResponse("Hello, Irina")

def danil(request):
    return HttpResponse("Hello, Danil")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
   
    })