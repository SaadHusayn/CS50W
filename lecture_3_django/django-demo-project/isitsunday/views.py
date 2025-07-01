from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    today = datetime.date.today()
    day_of_week = today.weekday()
    return render(request, "isitsunday/index.html", {"answer": day_of_week==6})
