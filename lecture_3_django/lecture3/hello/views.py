from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def saad(request):
    return HttpResponse("Hello Saad")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")
