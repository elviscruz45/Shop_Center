from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages

# Create your views here.

# def authentication(request):
#    return render(request,"login/login.html")


class VRegister(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,"signin/signin.html",{"form":form})

    def post(self,request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            login(request,usuario)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            
            return render(request,"signin/signin.html",{"form":form})

def exit_session(request):
    logout(request)
    return redirect("home")


def log_in(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            name_user=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=name_user,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"user no valid")
        else:
            messages.error(request,"Info invalid")                
    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})






