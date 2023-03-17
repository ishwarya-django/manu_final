from django.db import models
from CRM.models import Customer

# Create your models here.

STATUS_CHOICES=(
    ('profit','profit'),
     ('loss','loss'),
)

MEASURE_CHOICES=(
    ('kg','kg'),
    ('gram','gram'),
    ('litre','litre'),
    ('millilitre','millilitre'),

     
)
TYPE_CHOICES=(
    ('Manufactured_product','Manufactured_product'),
    ('Buy_product','Buy_product'),

)

# class Manufacturing(models.Model):
   

#     charges_name=models.CharField(max_length=20,null=True,blank=True)
#     charges_amount=models.DecimalField(max_digits = 16, decimal_places = 2,null=True, blank=True)
   
#     total_amount=models.DecimalField(max_digits = 16, decimal_places = 2,null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
class Product(models.Model):
    manufactured_product=models.CharField(max_length=20)
    manufactured_quantity=models.CharField(max_length=60)
    measure=models.CharField(choices = MEASURE_CHOICES,max_length=60)
    type_name=models.CharField(max_length=20,choices=TYPE_CHOICES,null=True,blank=True)


    total_charge_amount=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    raw_material_amount=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    sell_status=models.CharField(max_length=20,choices=STATUS_CHOICES,null=True,blank=True)
    status= models.CharField(choices=STATUS_CHOICES,max_length=100, null=True,blank=True)
    price_pro_loss=models.DecimalField(max_digits = 8,decimal_places = 2,default=0)
    total_manufactured_amount=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    total_sell_amount=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    sub_amount=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    unit_purchase_price=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    sell_quantity=models.IntegerField(null=True, blank=True,default=0)
    unit_price_manu_product=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    quantity_price=models.IntegerField(null=True, blank=True,default=0)

    #
    purchase_price=models.DecimalField(max_digits = 8,decimal_places = 2,default=0)
    # purchase_quantity=models.IntegerField(null=True, blank=True,default=0)





    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Manufacturing(models.Model):
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)

    charges_name=models.CharField(max_length=20)
    charges_amount=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    
    
    Date=models.DateTimeField(auto_now_add=True)

STATUS_SELL_CHOICES=(
     ('New','New'),
     ('Confirmed','Confirmed'),
     ('Cancelled','Cancelled'),

)

class SellProduct(models.Model):
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    sell_quantity=models.IntegerField()
    quantity_price=models.IntegerField()
    total_sell_amount=models.DecimalField(max_digits = 16, decimal_places = 2,default=0)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    status_Sell=models.CharField(choices=STATUS_SELL_CHOICES,max_length=80,default='New')
    Date=models.DateTimeField(auto_now_add=True,null=True)




    
