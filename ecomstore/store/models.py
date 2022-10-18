from contextlib import nullcontext
from datetime import datetime
import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) 
    name=models.CharField(max_length=128,) 
    email=models.EmailField() 

    def __str__(self):
        return self.name 

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField() 
    digital=models.BooleanField(default=False, blank=True, null=True) 
    image=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name  

    @property
    def imageURL(self):
        try:
            url=self.image.url 
        except:
            url="" 
        return url 

class Order(models.Model):
    customer =models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered =models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default=False)
    transaction_id= models.CharField(max_length=100, null=True) 

    def __str__(self):
        return str(self.id) 
    @property 
    def get_cart_total(self):
        orderitems =self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems]) 
        return total

    @property
    def get_cart_items(self):
        orderitems =self.orderitem_set.all()
        total =sum([item.quantity for item in orderitems])
        return total

     


class OrderItem(models.Model):
    product  =models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    order=models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered =models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True) 

    @property
    def get_total(self):
        total=self.product.price * self.quantity  
        return total

class ShippingAddress(models.Model):
    customer =models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    order =models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)
    address =models.CharField(max_length=200, blank=True, null=True)
    city =models.CharField(max_length=50, blank=True, null=True)
    zip_code =models.CharField(max_length=200,blank=True, null=True)
    state =models.CharField(max_length=50, null=True, blank=True)
    date_added =models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.address