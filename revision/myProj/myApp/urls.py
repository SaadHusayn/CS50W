from django.urls import path
from . import views

app_name = "myApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("taha/", views.taha, name="taha"),
    path("aashir/", views.aashir, name="aashir"),
    path("<str:name>", views.greet, name="greet")
]
