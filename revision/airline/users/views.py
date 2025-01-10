from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        #get username and password from the form
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if not user:
            #invalid credentials
            return render(request, "users/login.html", {"message":"Invalid Credentials."})
        
        #valid user then proceed to user details
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    #get request means to render a login page
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message":"Logged Out."})