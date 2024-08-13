from django.urls import path
from . import views
from django.shortcuts import render

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]