from django.core.serializers import serialize
import json
from django.db.models import Value
from django.db.models.functions import Replace, Lower
from django.shortcuts import render,redirect
from Menu.models import MenuItem
from Customers.models import Customer
from .models import Order,OrderItem

# Create your views here.
def display_orders(request):
    totalprice = {}
    orders = Order.objects.all().order_by('-created_at')
    orders = orders.prefetch_related('order_items__menu_item')
    for order in orders:
        for item in order.order_items.all():
            item.total_price = item.menu_item.price * item.quantity
        order.totalprice = sum(item.total_price for item in order.order_items.all())
    return render(request, 'display_order.html', {'orders': orders})

def add_order(request):
    Items = list(MenuItem.objects.all().values())
    Customers = list(Customer.objects.all().values())
    if request.method == "POST":
        data = json.loads(request.POST.get('order'))
        customer_name = data.get('customer_name')
        customer_phone = data.get('customer_phone')
        items = data.get('items')
        customer = Customer.getcustomer(name=customer_name, phone=customer_phone)
        order = Order.objects.create(customer=customer, customer_name=customer_name, customer_phone=customer_phone)
        for item_name, quantity in items.items():
            menu_item = MenuItem.get_menu_item(item_name=item_name)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
        return redirect('order_home')
    return render(request, 'add_order.html', {'menu_items': Items, 'customers':Customers})

def edit_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = order.order_items.all().select_related('menu_item')
    order_dict = {
        'customer_name': order.customer_name,
        'customer_phone': order.customer_phone,
        'items': {item.menu_item.item_name: item.quantity for item in order_items},
        'total_price': sum(item.menu_item.price * item.quantity for item in order_items)
    }
    if request.method == "POST":
        data = json.loads(request.POST.get('order'))
        customer_name = data.get('customer_name')
        customer_phone = data.get('customer_phone')
        items = data.get('items')
        customer = Customer.getcustomer(name=customer_name, phone=customer_phone)
        order.customer = customer
        order.customer_name = customer_name
        order.customer_phone = customer_phone
        order.save()
        order.order_items.all().delete()
        for item_name, quantity in items.items():
            menu_item = MenuItem.get_menu_item(item_name=item_name)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
        return redirect('order_home')
    return render(request, 'edit_order.html', {'order': order_dict, 'menu_items': list(MenuItem.objects.all().values())})

def delete_order(request, order_id):
    Order.objects.get(id=order_id).delete()
    return redirect('order_home')

def search_customer_order(request):
    customer = request.GET.get("name", "").strip()
    order = Order.objects.annotate(
        normalized_name=Lower(Replace("customer_name", Value(" "), Value("")))
    ).filter(
        normalized_name__icontains=customer
    )
    order = order.order_by('-created_at')
    orders = order.prefetch_related('order_items__menu_item')
    for order in orders:
        for item in order.order_items.all():
            item.total_price = item.menu_item.price * item.quantity
        order.totalprice = sum(item.total_price for item in order.order_items.all())
    return render(request, 'display_order.html', {'orders': orders})

