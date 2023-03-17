from django.shortcuts import render
from manu.models import Product
from CRM.models  import Customer

# Create your views here.
def order(request):
    x=Product.objects.all()
    y=Customer.objects.filter(is_active=True)
    
    return render (request,'order/make_order.html',{'x':x,'y':y})