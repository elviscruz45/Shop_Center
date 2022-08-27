from django.urls import path
from contact import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.Contact,name="contact"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


