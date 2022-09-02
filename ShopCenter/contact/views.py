from django.shortcuts import render,redirect
from .forms import FormContact
from django.core.mail import EmailMessage

# Create your views here.

def Contact(request):
    form_contact=FormContact()
    if request.method=="POST":
        form_contact=FormContact(data=request.POST)
        if form_contact.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")
            
            emailing=EmailMessage("Mensaje desde app Django",
                                  "El usuario con nombre {} con la direccion{} escribe lo siguiente: \n \n {}".format(name,email,content),"",["elviscruz45@gmail.com"],reply_to=[email])

            try:
                emailing.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?novalid")

    return render(request,"contact/contact.html",{"form":form_contact})
