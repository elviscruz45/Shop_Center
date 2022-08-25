from django.urls import path
from WebCenter import views



urlpatterns = [
    path('', views.home,name="home"),
    path('service', views.Services,name="services"),
    path('shop', views.Shop,name="shop"),
    path('blog', views.Blog,name="blog"),
    path('contact', views.Contact,name="contact"),
    
]
