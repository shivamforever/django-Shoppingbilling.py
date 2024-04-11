from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name="product_list_create"),
    
    path('products/<int:pk>', ProductRetrieveUpdateDestroyView.as_view(), name="product_detail"),
    
    path('customers/', CustomerListCreateView.as_view(), name="customer_list_create"),
    
    path('customers/<int:pk>', CustomerRetrieveUpdateDestroyView.as_view(), name="customer_detail"),
    
    path('bill/', GenerateBillView.as_view(), name="bill"),
    
    path('bill/<int:pk>', BillRetrieveUpdateDestroyView.as_view(), name="bill_detailed"),
]
