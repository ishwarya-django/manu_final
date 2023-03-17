from django.db import models
from manu.models import Product
from CRM.models import Customer
ORDER_CHOICES=(
     ('New','New'),
     ('Confirmed','Confirmed'),
     ('Cancelled','Cancelled'),
     ('Inprogress','Inprogress'),
     ('Completed','Completed'),
)
class MakeOrder(models.Model):
     customer= models.ForeignKey(Customer,max_length=190,null=True,on_delete=models.CASCADE)
     order_number=models.CharField(max_length=20,null=True)
     status=models.CharField(choices=ORDER_CHOICES,max_length=160,default='New')
     created_at = models.DateTimeField(auto_now_add=True,null=True)
     updated_at = models.DateTimeField(auto_now=True,null=True)

class Order_product(models.Model):
    order= models.ForeignKey(MakeOrder,on_delete=models.CASCADE,max_length=160,null=True)
    customer=models.ForeignKey(Customer,max_length=190,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,max_length=160,null=True)
    quantity=models.CharField(max_length=100,null=True)
    product_amount=models.DecimalField(max_digits = 14,decimal_places = 2,default=0)
    total_amount=models.DecimalField(max_digits = 14,decimal_places = 2,default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
