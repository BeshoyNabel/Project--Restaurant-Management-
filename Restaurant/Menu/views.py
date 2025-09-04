from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Value
from django.db.models.functions import Replace, Lower
from .models import MenuItem

# Create your views here.
def DisplayMenuItems(request):
    menu_items = MenuItem.get_all_menu_items()
    return render(request, 'display_items.html', {'menu_items': menu_items})
def AddMenuItem(request):
    if request.method == 'POST':
        name = request.POST.get('Mitem')
        price = request.POST.get('Mprice')
        description = request.POST.get('MDS')
        item = MenuItem.objects.filter(item_name=name).first()
        if item:
            messages.success(request, "Item is already exist.")
            return render(request, 'add_item.html')
        MenuItem.create_menu_item(name, price, description)
        return redirect('menu_home')
    return render(request, 'add_item.html')
def EditMenuItem(request, item_name):
    menu_item = MenuItem.objects.get(item_name=item_name)
    if request.method == 'POST':
        name = request.POST.get('Mitem')
        price = request.POST.get('Mprice')
        description = request.POST.get('MDS')
        item = MenuItem.objects.filter(item_name=name).exclude(item_name=menu_item.item_name).first()
        if item:
            messages.success(request, "Item is already exist.")
            return render(request, 'edit_item.html', {'menu_item': menu_item})
        menu_item.item_name = name
        menu_item.price = price
        menu_item.description = description
        menu_item.save()
        return redirect('menu_home')
    return render(request, 'edit_item.html', {'menu_item': menu_item})
def DeleteMenuItem(request, item_name):
    MenuItem.objects.get(item_name=item_name).delete()
    return redirect('menu_home')

def SearchMenuItem(request):
    item = request.GET.get("name", "").strip()
    items = MenuItem.objects.annotate(
        normalized_name=Lower(Replace("item_name", Value(" "), Value("")))
    ).filter(
        normalized_name__icontains=item
    )
    return render(request, 'display_items.html', {'menu_items': items})