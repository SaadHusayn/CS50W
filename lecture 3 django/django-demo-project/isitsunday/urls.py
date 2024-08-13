from django.urls import path
from . import views

app_name = "isitsunday"

urlpatterns = [
    path('', views.index, name="index")
]