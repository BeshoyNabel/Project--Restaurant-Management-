from django.urls import path

from .views import *

urlpatterns = [
    path('', display_orders, name='order_home'),
    path('add_order/', add_order, name='add_order'),
    path('edit_order/<int:order_id>/', edit_order, name='edit_order'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
    path('search/', search_customer_order, name='search_customer_order')
]