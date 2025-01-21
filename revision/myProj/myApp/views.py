from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import requests

# Create your views here.
def index(request):
    return render(request, 'myApp/index.html')

sectionData = ['data of section 1', 'data of section 2', 'data of section 3']

def section(request, id):
    if (id >0 and  id<=3):
        return HttpResponse(sectionData[id-1])
    else:
        return Http404('section not found')


def factsAPI(request, limit):
    try:
        response = requests.get(f"https://catfact.ninja/facts?limit={limit}")
        if response.status_code != 200:
            raise Exception(f"HTTP ERROR!!, Status Code {response.status_code}")
        
        data = response.json()
        return JsonResponse({"facts":data["data"]})
    except Exception as e:
        print(f"Error getting facts: {e}")
        return Http404("no facts")
    
