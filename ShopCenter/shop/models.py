from django.db import models


class CatProd(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="catprod"
        verbose_name_plural="categoria_Productos"
    def __str__(self):
        return self.name
    



class Product(models.Model):
    name=models.CharField(max_length=50)
    cat=models.ForeignKey(CatProd,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="shop",null=True,blank=True)
    price=models.FloatField()
    availability=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="product"
        verbose_name_plural="products"
    def __str__(self):
        return self.name

