from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post
from .forms import PostForm


def index(request):
    return render(request, "network/index.html", {"form": PostForm(), "posts":Post.objects.all().order_by('-created_at')})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def create_post(request):
    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.creator = request.user
            post.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/index.html", {"form": postForm, "posts":Post.objects.all().order_by('-created_at')})
    else:
        return HttpResponseNotFound('not allowed :(')


def user_profile(request, username):
    try:
        user = User.objects.get(username = username)
    except:
         return HttpResponseNotFound('not allowed :(')
    
    return render(request, 'network/profile.html',{"userData":user, "posts":user.posts.all().order_by('-created_at')})

def follow(request):
    if request.method != "POST":
        #redirect to the home page
        return HttpResponseRedirect(reverse("index"))

    user1 = request.user
    user2 = User.objects.get(pk = request.POST["user2ID"])
    toFollow = int(request.POST["toFollow"])

    #if toFollow is true, user1 follows user2
    #if toFollow is false, user1 unfollows user2
    if toFollow:
        if not user2 in user1.following.all():
            user2.add_follower(user1)
    else:
        if user2 in user1.following.all():
            #user1 is unfollowing user2
            user1.following.remove(user2)
    
    return HttpResponseRedirect(reverse("userProfile", args=(user2.username, )))




