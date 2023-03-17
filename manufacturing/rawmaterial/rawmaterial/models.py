from django.db import models

from manu.models  import Product



MEASURE_CHOICES=(
    ('kg','kg'),
    ('gram','gram'),
    ('litre','litre'),
    ('millilitre','millilitre'),

     
)
# Create your models here.
class Raw_material(models.Model):
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    material=models.CharField(max_length=300,null=True)
    unit_price=models.DecimalField(max_digits = 8,decimal_places = 2,default=0)
    quantity=models.IntegerField()
    measure=models.CharField(choices = MEASURE_CHOICES,max_length=60,null=True)
    total_price=models.DecimalField(max_digits = 8,decimal_places = 2,default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.material}"


STATUS_CHOICES= (
    ('profit', 'profit'),
    ('loss', 'loss'),
    
    )

class Purchase_product(models. Model):
    org_product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    price_pro_fromshop=models.DecimalField(max_digits = 8,decimal_places = 2,default=0)
    status= models.CharField(choices=STATUS_CHOICES,max_length=100, null=True,blank=True)
    price_pro_loss=models.DecimalField(max_digits = 8,decimal_places = 2,default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f"{self.org_product}"