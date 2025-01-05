from django.shortcuts import render

tasks = ["work on web dev", "take crypto class", "trump cards"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks":tasks
    })

def add(request):
    return render(request, "tasks/add.html")