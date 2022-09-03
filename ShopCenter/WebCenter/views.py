from django.shortcuts import render, HttpResponse
from services.models import Service
from marketcar.car import Car

def home(request):
    car=Car(request)
    return render(request,"WebCenter/home.html")

