from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my homepage of the project")