from django.urls import path
from WebCenter import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home,name="home"),
    path('shop/', views.Shop,name="shop"),
    path('contact/', views.Contact,name="contact"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


