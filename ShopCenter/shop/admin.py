from django.contrib import admin
from .models import CatProd,Product

# Register your models here.




class CatProdAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


class ProductAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(CatProd,CatProdAdmin)

admin.site.register(Product,ProductAdmin)
