from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"WebCenter/home.html")

def Services(request):
    return render(request,"WebCenter/services.html",)

def Shop(request):
    return render(request,"WebCenter/shop.html",)

def Blog(request):
    return render(request,"WebCenter/blog.html",)

def Contact(request):
    return render(request,"WebCenter/contact.html",)
    
