from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flask import redirect
from marketcar.car import Car
from django.contrib import messages
from delivery.models import Requestt, OnlineRequest

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url="/authentication/login")
def request_process(request):
    request_1=Requestt.objects.create(user=request.user)
    car=Car(request)
    online_request=list()
    for key, value in car.car.items():
        online_request.append(OnlineRequest(
            product_id=key,
            quantity=value["quantity"],
            user=request.user,
            requestt=request_1
        ))
        
    send_emaill(
        requestt=request_1,
        online_request=online_request,
        user_name=request.user.username,
        user_email=request.user.email
    )
    messages.success(request,"The delivy has been send...")
    return redirect("../shop")

def send_emaill(**kwargs):
    subject="thanks for the requestment"
    message=render_to_string("emails/delivery.html",{
        "delivery":kwargs.get("requestt"),
        "online_request":kwargs.get("online_request"),
        "user_name":kwargs.get("user_name")
    })
    text_message=strip_tags(message)
    from_email="teseosoftwarecompany@gmail.com"
    #to=kwargs.get(user_name)
    to="elviscruz45@gmail.com"
    send_mail(subject,text_message,from_email,[to],html_message=message)