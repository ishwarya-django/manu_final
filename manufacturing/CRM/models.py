from django.db import models



# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=80,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    email=models.EmailField(unique=True)
    doorno=models.CharField(max_length=50,null=True)
    address_line1=models.CharField(max_length=50,null=True)
    address_line2=models.CharField(max_length=50,null=True)
    organization=models.CharField(max_length=50,null=True)

    place=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
    pincode=models.CharField(max_length=6,null=True)
    state=models.CharField(max_length=50,null=True)
    country=models.CharField(max_length=50,null=True)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return f"{self.name}"

