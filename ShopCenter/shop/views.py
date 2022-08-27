from django.shortcuts import render
from .models import Product,CatProd

# Create your views here.

def Shop(request):
    products=Product.objects.all()
    return render(request,"shop/shop.html",{"products":products})


