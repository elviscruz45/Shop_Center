from itertools import product
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product
from django.db.models import F,Sum,FloatField


User=get_user_model()

class Requestt(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id 
    
    @property
    def total(self):
        return self.onlinerequest_set.aggregate(
            total=Sum(F("price")*F("quantity"),output_field=FloatField())
        )["total"]
    
    class Meta:
        db_table="request"
        verbose_name="request"
        verbose_name_plural="requests"
        ordering=["id"]

class OnlineRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    request=models.ForeignKey(Requestt,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} unidades de {self.product.name}"
    
    class Meta:
        db_table="onlinerequest"
        verbose_name="Online Request"
        verbose_name_plural="Online Requests"
        ordering=["id"]
        
        