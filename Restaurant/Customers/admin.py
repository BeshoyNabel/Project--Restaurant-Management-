from django.contrib import admin
from .models import Customer

# Register your models here.
admin.site.site_header = "Customer Management"
admin.site.register(Customer)