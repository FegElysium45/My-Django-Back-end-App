from django.shortcuts import render



# Create your views here.
from django.http import HttpResponse 

def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp. My second Application. Azuks!") 

def home(request): 
    return render(request, "home.html", {}) 

def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 