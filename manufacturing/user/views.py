from django.shortcuts import render,redirect
from django.contrib import messages, auth
from.models import User
from django.contrib.auth.models import Group
from.forms import RegistrationForm,Role_assign_Form
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def layout(request):
    return render(request,'user/layout.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        role=request.POST.get('role')
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role=form.cleaned_data['role']
            confirm_password = form.cleaned_data.get('confirm_password')
            username = email.split("@")[0]
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password,role=role)
            user.phone_number = phone_number
            user.save()
            return redirect('login')    
        else:
            form = RegistrationForm()
            context = {
                     'form': form,
                     'role':role,
                         }
            return render(request, 'user/register.html', context)  
    else:
        form = RegistrationForm()
    context = {
        'form': form,
       
    }
    return render(request, 'user/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            messages.success(request,f"Welcome {user.username}")
            return redirect('layout')
        else:
            err="Enter correct username and password "
            return render(request,'user/login.html',{'err':err})
    return render(request,'user/login.html')

@login_required(login_url = 'login')
def logout_view(request):
    auth.logout(request)
    return redirect('login')

def assign_role(request):
    x=User.objects.all().exclude(is_superadmin=True)
    y=Group.objects.all()
    form=Role_assign_Form()
    if request.method=="POST":
        x=User.objects.all().exclude(is_superadmin=True)
        y=Group.objects.all()
        form= Role_assign_Form(request.POST)
        if form.is_valid():
            grp=request.POST.get('group')
            print(grp)
            use=request.POST.get('user')
            print(use)
            user=User.objects.get(id=use)
            selected_group = Group.objects.get(id=grp) 
            selected_group.user_set.add(user)  
            user.group = selected_group
            user.save()
            form.save()
            messages.success(request,f"{selected_group.name} role assigned for  {user.username} successfully")
            return render(request,'user/assign_role.html',{'x':x,'y':y})
        else:
             return render(request,'user/assign_role.html',{'x':x,'y':y,'form':form})
    else:
        return render(request,'user/assign_role.html',{'x':x,'y':y,'form':form})

 