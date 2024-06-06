from django.contrib import admin
from django.urls import path
from . import views
from blog.models import Customer
from blog.views import index, product_detail, customer_list, customer_details, add_customer
 

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('customer/', customer_list, name='customer_list'),
    path('customer-detail/<int:pk>/', customer_details, name='customer_details'),
   path('add_customer/',add_customer, name = 'add_customer'),
]
