from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>THis is heading</h1>")

def generic(request, route):
    return HttpResponse(f"<h1>You are into {route.upper()} page</h1>")