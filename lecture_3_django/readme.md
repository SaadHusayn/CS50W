django-admin startproject PROJECTNAME
cd PROJECTNAME
python .\manage.py runserver
python .\manage.py startapp appname

in views.py of appname write functions (ex. index)
create urls.py in appname and add routes
urlpatterns = [
    path("", views.index, name="smthng")
]

include urls.py of myapp in Project's urls.py
path("appname\", include("appname.urls"))