from django.urls import path
from . import views

app_name = "myApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("section/<int:id>", views.section, name="section"),
    path("facts/<int:limit>", views.factsAPI, name="facts")
]
