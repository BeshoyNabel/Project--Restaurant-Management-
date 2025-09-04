from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
admin.site.site_header = "Order Management"
admin.site.register(Order)
admin.site.register(OrderItem)