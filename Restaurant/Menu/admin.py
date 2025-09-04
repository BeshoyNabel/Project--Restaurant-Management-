from django.contrib import admin
from .models import MenuItem

# Register your models here.
admin.site.site_header = "MenuItem Management"
admin.site.register(MenuItem)