from django.urls import path

from .views import *

urlpatterns = [
    path('', customer_home, name='customer_home'),
    path('add_customer/', add_customer, name='add_customer'),
    path('sort_customers/', sort_customers, name='sort_customers'),
    path('delete_customer/<str:name>/<str:phone>/', delete_customer, name='delete_customer'),
    path('edit_customer/<str:name>/<str:phone>/', edit_customer, name='edit_customer'),
    path('search/', search_customer, name='search_customer'),
    path('customer_orders/<str:name>/<str:phone>/', customer_orders, name='customer_orders'),
    path('customer_detail', customer_detail, name='customer_detail'),
    path('search_customer_orders/', search_customer_orders, name='search_customer_orders'),
]