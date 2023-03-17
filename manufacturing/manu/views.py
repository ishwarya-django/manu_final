from django.shortcuts import render,redirect
from .forms import ChargeForm,ProductForm,SoldForm,ByProductForm
from django.contrib import messages
from.models import Manufacturing,Product,SellProduct
from rawmaterial.models import Raw_material
from CRM.models import Customer



# Create your views here.


def product(request):
    product=Product.objects.filter(type_name="Manufactured_product")
    # product=Product.objects.all()

    if request.method=="POST":
      
        form = ProductForm(request.POST) 
        q=request.POST.get("manufactured_product")    
        print(q)  
          
        if form.is_valid():  
            x=form.save()
            x.type_name=  "Manufactured_product"   
            x.save()                
            messages.success(request, 'Added successfully') 
            return redirect('product')            
         
        else:
            print(form.errors)
            return render(request,'manu/product.html',{'product':product,'form':form})             
    else:        
        form=ProductForm()
        return render(request,'manu/product.html',{'product':product,'form':form}) 

def by_product(request):
    product=Product.objects.filter(type_name="Buy_product")

    if request.method=="POST":
      
        form = ByProductForm(request.POST) 
        q=request.POST.get("manufactured_product")    
        print(q)  
          
        if form.is_valid():  
            x=form.save()
            x.type_name=  "Buy_product"   
            x.save()                
            messages.success(request, 'Added successfully') 
            return redirect('by_product')            
         
        else:
            print(form.errors)
            return render(request,'manu/by_product.html',{'product':product,'form':form})             
    else:        
        form=ProductForm()
        return render(request,'manu/by_product.html',{'product':product,'form':form})        

def manufacture(request,id):
   raw_material=Raw_material.objects.filter(product_name_id=id)
   product=Product.objects.get(id=id)
   manufacture=Manufacturing.objects.filter(product_name_id=id)
   if request.method=="POST":
        form = ChargeForm(request.POST)          
        if form.is_valid():
            
            x=form.save()  
            x.product_name_id=id
            x.save()  
            
            total=0
            for i in manufacture:
              total+=i.charges_amount
              product.total_charge_amount=total
              product.save()
        
            # raw=0
            # for i in raw_material:
            #   raw+=i.total_price
            #   print(raw)
            
            product.total_manufactured_amount=total+product.raw_material_amount
            
            # add=total+raw
           
            # product.total_manufactured_amount=add
            
            
            


            product.save()
            messages.success(request,'charges added successfully')
            return render(request,'manu/manufacturing.html', {'product':product,'total_charge_amount':total,'manufacture':manufacture,'product':product})             
         
 
        else:
           
            return render(request,'manu/manufacturing.html', {'form':form,'manufacture':manufacture,'product':product})            
   else:        
        form=ChargeForm()
        return render(request, 'manu/manufacturing.html',{'manufacture':manufacture,'product':product}) 



def sell_product(request,id):
    product=Product.objects.get(id=id)
    sell_product=SellProduct.objects.filter(product_name_id=id)
    y=Customer.objects.filter(is_active=True)
    if request.method=="POST":
        form = SoldForm(request.POST)  
        s=request.POST.get("sell_quantity")
        print(s)
        t=request.POST.get("quantity_price")
        print(t)
        q=request.POST.get("total_sell_amount")
        customer=request.POST.get('customer')
        print(q)
        msg=[]
        x=0  
        for i in sell_product:
            x+=i.sell_quantity
        if (x + int(s)) > product.manufactured_quantity:
            count= product.manufactured_quantity - x 
            msg.append( f'{count} product  only  in stock ')
            return render(request,'manu/sell_product.html',{'product':product,'sell_product':sell_product,'msg':msg,'form':form,'customer':customer,'y':y})   
        if form.is_valid():       
            sell_product=SellProduct.objects.filter(product_name_id=id)
            y=form.save()
            y.status_Sell='New'
            y.product_name_id=id  
            y.total_sell_amount=y.sell_quantity*y.quantity_price
            y.save() 
            total_sell=0
            sell_quant=0
            quan_price=0
            for i in sell_product:
                total_sell+=i.total_sell_amount
                product.total_sell_amount=total_sell
                sell_quant+=i.sell_quantity
                product.sell_quantity=sell_quant
                quan_price+=i.quantity_price
                product.quantity_price=quan_price
                product.save()
            if product.total_manufactured_amount> product.total_sell_amount:
                sub=product.total_manufactured_amount-product.total_sell_amount
                product.sub_amount=sub
                product.sell_status="Loss"
                product.save()
            elif product.total_manufactured_amount< product.total_sell_amount:
                product.sell_status="Profit"
                sub=product.total_sell_amount-product.total_manufactured_amount
                product.sub_amount=sub
                product.save()
            messages.success(request,'Added sucessfully')
            return render(request,'manu/sell_product.html',{'product':product,'sell_product':sell_product})            
        else:
            print(form.errors)
            return render(request,'manu/sell_product.html',{'form':form,'product':product,'sell_product':sell_product,'customer':customer,'y':y})             
    else:        
        form=SoldForm()
        return render(request, 'manu/sell_product.html',{'product':product,'sell_product':sell_product,'form':form,'y':y}) 


def edit_product(request,id):
    edit_product=Product.objects.get(id=id)
    form=ProductForm(instance=edit_product)
    
    if request.method=="POST":
        form=ProductForm(request.POST,instance=edit_product)
        if form.is_valid():
            edit=form.save()
            edit.save()
            return redirect('product')
        else:
            print(form.errors)
            return render(request,"manu/edit_product.html",{'edit_product':edit_product,'form':form})
    else:
        
        return render(request,"manu/edit_product.html",{'edit_product':edit_product,'form':form})

def delete_product(request,id):
    x = Product.objects.get(id=id)
    x.delete()
    return redirect('product') 

def soldproduct_details(request):
    product=Product.objects.filter(type_name="Manufactured_product")
    
    

    return render(request,"manu/soldproduct_details.html",{'product':product})

def edit_byproduct(request,id):
    edit_product=Product.objects.get(id=id)
    form=ProductForm(instance=edit_product)
    
    if request.method=="POST":
        form=ProductForm(request.POST,instance=edit_product)
        if form.is_valid():
            edit=form.save()
            edit.save()
            return redirect('by_product')
        else:
            print(form.errors)
            return render(request,"manu/edit_product.html",{'edit_product':edit_product,'form':form})
    else:
        
        return render(request,"manu/edit_product.html",{'edit_product':edit_product,'form':form})

def delete_byproduct(request,id):
    x = Product.objects.get(id=id)
    x.delete()
    return redirect('by_product') 


def purchase_sold_detail(request):
    x=Product.objects.filter(type_name="Buy_product")
    
    return render(request,"manu/sold_purchasepro.html",{'x':x})


def sell_product_pur(request,id):
    product= Product.objects.get(id=id)
    sell_product=SellProduct.objects.filter(product_name_id=id)
    y=Customer.objects.filter(is_active=True)
    if request.method=="POST":
        form = SoldForm(request.POST)  
        s=request.POST.get("sell_quantity")
        print(s)
        t=request.POST.get("quantity_price")
        print(t)
        q=request.POST.get("total_sell_amount")
        customer=request.POST.get('customer')
        print(q)
        msg=[]
        x=0  
        for i in sell_product:
            x+=i.sell_quantity
        if (int(x) + int(s)) > int(product.manufactured_quantity):
            count= int(product.manufactured_quantity) - int(x)
            msg.append( f'{count} product  only  in stock ')
            return render(request,'manu/sell_product.html',{'product':product,'sell_product':sell_product,'msg':msg,'form':form,'customer':customer,'y':y})   
        if form.is_valid():       
            sell_product=SellProduct.objects.filter(product_name_id=id)
            y=form.save()
            y.status_Sell='New'
            y.product_name_id=id  
            y.total_sell_amount=y.sell_quantity*y.quantity_price
            y.save() 

            total_sell=0
            sell_quant=0
            quan_price=0
            for i in sell_product:
                total_sell+=i.total_sell_amount
                product.total_sell_amount=total_sell
                sell_quant+=i.sell_quantity
                product.sell_quantity=sell_quant
                quan_price+=i.quantity_price
                product.quantity_price=quan_price
                product.save()

            messages.success(request,'Added sucessfully')
            return render(request,'manu/sell_purchse.html',{'product':product,'sell_product':sell_product})            
        else:
            print(form.errors)
            return render(request,'manu/sell_purchse.html',{'form':form,'product':product,'sell_product':sell_product,'customer':customer,'y':y})  

    return render(request, 'manu/sell_purchse.html',{'product':product,'sell_product':sell_product,'y':y}) 

