from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} ({self.code})"
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} -> {self.destination}"
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self): 
        return f"{self.first} {self.last}"
