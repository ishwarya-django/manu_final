from django.shortcuts import render,redirect
from django.contrib import messages
from.models import Customer
from.forms import Customer_Form
from manu.models import SellProduct

# Create your views here.
def add_customer(request):
    form=Customer_Form()
    if request.method=="POST":
        form=Customer_Form(request.POST)
        if form.is_valid():
            name= request.POST.get('name')
            form.save()
            messages.success(request,f"{name} customer added successfully")
            return redirect('view_customer')
        else:
            return render(request,'crm/add_customer.html',{'form':form})
    return render(request,'crm/add_customer.html')

def view_customer(request):
    customer=Customer.objects.all() 
    return render(request,'crm/view_customer.html',{'customer':customer})

def edit_customer(request,id):
    customer=Customer.objects.get(id=id) 
    if request.method=="POST":
        form=Customer_Form(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request,'updated successfully')
            return redirect('view_customer')
        return render(request,'crm/edit_customer.html',{'customer':customer,'form':form})
    return render(request,'crm/edit_customer.html',{'customer':customer})

def customer_purchase_details(request):
    customer=Customer.objects.filter(is_active=True) 
    return render(request,'crm/purchase_detail.html',{'customer':customer})

def purchase_product_customer(request,id):
    product=SellProduct.objects.filter(customer=id)
    return render(request,'crm/purchase_product_customer.html',{'product':product})
    
def deactivate_customer(request,id):
    customer=Customer.objects.get(id=id)
    customer.is_active= False
    customer.save()   
    return redirect('view_customer') 
def activate_customer(request,id):
    customer=Customer.objects.get(id=id)
    customer.is_active= True
    customer.save()   
    return redirect('view_customer') 

def customer_purchase(request):
    x=Customer.objects.filter(is_active=True)
    if request.method=="POST":
        customer=request.POST.get('customer')
        y=SellProduct.objects.filter(customer= customer)
        return render(request,'crm/cus_pur.html',{'x':x,'y':y})

    return render(request,'crm/cus_pur.html',{'x':x})