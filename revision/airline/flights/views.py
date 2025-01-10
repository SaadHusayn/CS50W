from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights":Flight.objects.all()
    })

def flight(request, id):
    try:
        desiredFlight = Flight.objects.get(pk=id)
    except:
        raise Http404("flight not found")
    
    return render(request, "flights/flight.html", {
        "flight": desiredFlight,
        "passengers":desiredFlight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=desiredFlight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flightObj = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flightObj)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight_id, )))
