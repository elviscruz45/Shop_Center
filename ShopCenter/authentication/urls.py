from django.urls import path
from .views import VRegister,exit_session,log_in

urlpatterns = [
    path("",VRegister.as_view(),name="authentication"),
    path("exit",exit_session,name="exit"),
    path("login",log_in,name="login"),

]
