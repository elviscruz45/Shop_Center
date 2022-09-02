from django.urls import path
from . import views

app_name="car"

urlpatterns=[
    path("add/<int:product_id>",views.add_product,name="add"),
    path("delete/<int:product_id>",views.delete_product,name="delete"),
    path("quit/<int:product_id>",views.quit_product,name="quit"),
    path("clean/<int:product_id>",views.clean_product,name="clean"),
]
