
from django.urls import path,include
from.import views


urlpatterns = [
  path('add_customer/',views.add_customer,name="add_customer"),
  path('view_customer/',views.view_customer,name="view_customer"),
  path('edit_customer/<int:id>/',views.edit_customer,name="edit_customer"),
  path('deactivate_customer/<int:id>/',views.deactivate_customer,name="deactivate_customer"),
  path('activate_customer/<int:id>/',views.activate_customer,name="activate_customer"),
  path('customer_purchase_details/',views.customer_purchase_details,name="customer_purchase_details"),
  path('purchase_product_customer/<int:id>/',views.purchase_product_customer,name="purchase_product_customer"),
  path('customer_purchase/',views.customer_purchase,name="customer_purchase"),
]