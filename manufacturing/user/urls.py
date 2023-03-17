
from django.urls import path,include
from . import views

urlpatterns = [
    path('layout/',views.layout,name='layout'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('assign_role/',views.assign_role,name="assign_role"), 
]