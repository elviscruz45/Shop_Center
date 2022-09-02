from django.shortcuts import render
from marketcar.car import Car
from shop.models import Product
from django.shortcuts import redirect


def add_product(request,product_id):
    car=Car(request)
    product=Product.objects.get(id=product_id)
    car.add(product=product)
    return redirect("shop")

def delete_product(request,product_id):
    car=Car(request)
    product=Product.objects.get(id=product_id)
    car.delete(product=product)
    return redirect("shop")


def quit_product(request,product_id):
    car=Car(request)
    product=Product.objects.get(id=product_id)
    car.quit_product(product=product)
    return redirect("shop")

def clean_product(request,product_id):
    car=Car(request)
    car.clean_car()
    return redirect("shop")

