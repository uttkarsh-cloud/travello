from django.shortcuts import render
from .models import Destination
# Create your views here.
from django.http import JsonResponse
import json

def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

def check(request):
    dests = Destination.objects.all()
    listOfDest = []
    for i in dests:
        data = {
            "name": i.name,
            "desc": i.desc
        }
        listOfDest.append(data)
    resp = {
        "results": listOfDest
    }
    return JsonResponse(resp, safe=False)

def acceptResponse(request):
    if request.method == 'POST':
        y = json.loads(request.body)
        username = y["username"]
        age = y["age"]
        print(username, age)
        data = {
            "state": True
        }
        return JsonResponse(data, safe=False)