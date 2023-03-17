
from django.urls import path
from . import views

urlpatterns = [

    path('manufacture/<int:id>/', views.manufacture, name='manufacture'),
    path('', views.product, name='product'),
    path('sell_product/<int:id>/', views.sell_product, name='sell_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('soldproduct/', views.soldproduct_details, name='soldproduct_details'),
    path('by_product', views.by_product, name='by_product'),
     path('edit_byproduct/<int:id>/', views.edit_product, name='edit_byproduct'),
    path('delete_byproduct/<int:id>/', views.delete_byproduct, name='delete_byproduct'),
    path('purchase_sold_detail/', views.purchase_sold_detail, name='purchase_sold_detail'),
    path('sell_product_pur/<int:id>/', views.sell_product_pur, name='sell_product_pur'),
    
 





]