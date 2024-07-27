from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('sections/<int:sectionNumber>', views.section, name="section")
]