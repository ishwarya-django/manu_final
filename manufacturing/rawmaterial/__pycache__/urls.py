
from django.urls import path,include
from.import views


urlpatterns = [
   path('add_mat/<int:id>/',views.add_mat,name="add_mat"),
   path('delete/<int:id>/',views.edit_mat,name="edit_mat"),
   path('delete_raw/<int:id>/',views.delete_raw,name="delete_raw"),
   path('purchase_product/<int:id>',views.purchase_product,name="purchase_product"),
   path('view_product/',views.view_product,name="view_product"),

]