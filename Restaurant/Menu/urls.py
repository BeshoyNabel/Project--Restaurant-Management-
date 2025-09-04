from django.urls import path

from .views import *

urlpatterns = [
    path('', DisplayMenuItems, name='menu_home'),
    path('add/', AddMenuItem, name='add_menu_item'),
    path('edit/<str:item_name>/', EditMenuItem, name='edit_menu_item'),
    path('delete/<str:item_name>/', DeleteMenuItem, name='delete_menu_item'),
    path('search/', SearchMenuItem, name='search_menu_item')
]