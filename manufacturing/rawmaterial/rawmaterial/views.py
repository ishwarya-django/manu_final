from django.shortcuts import render,redirect,HttpResponse
from.models import Raw_material,Purchase_product
from.forms import Raw_material_Form,Purchase_product_form
from django.contrib import messages
from manu.models import Product

# Create your views here.
def add_mat(request,id):
    product=Product.objects.get(id=id)
    x=Raw_material.objects.filter(product_name_id=product.id)
    form=Raw_material_Form()
    if request.method=="POST":
        x=Raw_material.objects.filter(product_name_id=product.id)
        form=Raw_material_Form(request.POST)
        amt=[]
        msg=[]
        price= request.POST.get('unit_price')
        measure=request.POST.get('measure')  
        amt.append(price)
        
        try:
                typ = float(price)
                t=str(typ).split('.')[1]
                if len(t) > 2:
                    msg.append('more than 2 decimal_places')
                
                else:
                    msg.append(None)

        except:
                msg.append('enter a number')
        z=zip(amt,msg)
        for i in msg:
            if i is not None:
                return render(request,'raw/add_mat.html',{'z':z,'x':x,'form':form,'measure':measure})  
        measure=request.POST.get('measure')     
        if form.is_valid():
            mat=request.POST.get('material')
           
            y=form.save()
            y.total_price=y.unit_price*y.quantity
            y.product_name_id=product.id
            y.save()
            total_raw=0
            for i in x:
                total_raw += i.total_price
            product.raw_material_amount=total_raw
    
            product.save()
            product.total_manufactured_amount=product.total_charge_amount+total_raw
            product.unit_price_manu_product=float(product.total_manufactured_amount)/float(product.manufactured_quantity)
    
            product.save()
            if float(product.unit_price_manu_product) > float(product.unit_purchase_price):
        
                loss=float(product.unit_price_manu_product) - float(product.unit_purchase_price)
        
                product.status="loss"
                product.price_pro_loss=loss
                product.save()
             
            elif float(product.unit_price_manu_product) < float(product.unit_purchase_price):
               
                profit=float(product.unit_purchase_price) - float(product.unit_price_manu_product)
               
             
                product.status="profit"
                product.price_pro_loss=profit
                product.save()
            product.save()
            messages.success(request,f'{mat} added successfully')
            return render(request,'raw/add_mat.html',{'x':x})   
        else:
            return render(request,'raw/add_mat.html',{'x':x,'form':form,'measure':measure})     
    return render(request,'raw/add_mat.html',{'x':x,'product':product})

def edit_mat(request,id):
    product=Raw_material.objects.get(id=id)
    if request.method=="POST":
        product=Raw_material.objects.get(id=id)
        form=Raw_material_Form(request.POST)
        material=request.POST.get('material')
        quantity=request.POST.get('quantity')
        measure= request.POST.get('measure')
        price= request.POST.get('unit_price')
        amt=[]
        msg=[]
        amt.append(price)
        
        try:
                typ = float(price)
                t=str(typ).split('.')[1]
                if len(t) > 2:
                    msg.append('more than 2 decimal_places')
                
                else:
                    msg.append(None)

        except:
                msg.append('enter a number')
        z=zip(amt,msg)
        for i in msg:
            if i is not None:
                return render(request,'raw/edit_mat.html',{'z':z,'form':form,'product':product,'measure':measure})
        product.material=material
        product.quantity=quantity
        product.unit_price=price
        product.measure=measure
        product.total_price=float(product.quantity)* float(product.unit_price)
        product.save()
        messages.success(request,f'{material} update successfully')
        return render(request,'raw/edit_mat.html',{'product':product})
    else:
        return render(request,'raw/edit_mat.html',{'product':product})


def delete_raw(request,id):
    raw=Raw_material.objects.get(id=id)
    pro=Product.objects.get(id=raw.product_name_id)
    print(pro)
    x=Raw_material.objects.filter(product_name_id=pro.id)
    raw.delete()
    return render(request,'raw/add_mat.html',{'x':x})


def purchase_product(request,id):
    product=Product.objects.get(id=id)
    form=Purchase_product_form()
    if request.method=="POST":
        form=Purchase_product_form(request.POST)
        product=Product.objects.get(id=id)
        price= request.POST.get('price_pro_fromshop')
        amt=[]
        msg=[]
        amt.append(price)
        
        try:
                typ = float(price)
                t=str(typ).split('.')[1]
                if len(t) > 2:
                    msg.append('more than 2 decimal_places')
                
                else:
                    msg.append(None)

        except:
                msg.append('enter a number')
        z=zip(amt,msg)
        for i in msg:
            if i is not None:
                return render(request,'raw/purchase_pro.html',{'z':z,'form':form,'product':product})
        price= request.POST.get('price_pro_fromshop')
        if form.is_valid():
            y=form.save()
            y.org_product=product
            y.save()
            product.unit_purchase_price= y.price_pro_fromshop
            product.save()
            unit_manu=float(product.total_manufactured_amount) / float(product.manufactured_quantity)
            product.unit_price_manu_product=unit_manu
            product.save()
            if float(product.unit_price_manu_product) > float(price):
                y.status="loss"
                loss=float(product.unit_price_manu_product) - float(price)
                y.price_pro_loss=loss
                product.status="loss"
                product.price_pro_loss=loss
                product.save()
                y.save()
            elif float(product.unit_price_manu_product) < float(price):
                y.status="profit"
                profit=float(price) - float(product.unit_price_manu_product)
                y.price_pro_loss=profit
                y.save()
                product.status="profit"
                product.price_pro_loss=profit
                product.save()
            return redirect('view_product')
        else:
            return render(request,'raw/purchase_pro.html',{'product':product,'form':form})    
    return render(request,'raw/purchase_pro.html',{'product':product})

def view_product(request):
    pro=Product.objects.all()
    return render(request,'raw/view_pro.html',{'pro':pro}) 