from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Django Timeeeeee")

def greet(request, name):
    return render(request, "myApp/greet.html",{
        "name":name.capitalize(),
        "has5letters": len(name) == 5
    })

def taha(request):
    return HttpResponse(f"Hello Taha!")

def aashir(request):
    return HttpResponse(f"Hello Aashir!!")
