from django.shortcuts import render, HttpResponse
from services.models import Service 

def home(request):
    return render(request,"WebCenter/home.html")


def Shop(request):
    return render(request,"WebCenter/shop.html",)


