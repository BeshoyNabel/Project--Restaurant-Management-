from django.contrib import messages
from django.shortcuts import render,redirect
from django.db.models import Value
from django.db.models.functions import Replace, Lower
from .models import Customer
from Orders.models import Order,OrderItem
from Menu.models import MenuItem
from django.db.models import Count

# Create your views here.
def customer_home(request):
    customer = Customer.getallcustomer()
    return render(request, 'display_customer.html', {'customers': customer, 'sort_by': 'Desc', 'next_sort': 'Asc'})

def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get("Cname")
        phone = request.POST.get("Cphone")
        email = request.POST.get("Cemail")
        customer = Customer.objects.filter(name=name, phone=phone).first()
        if customer:
            messages.success(request, "Customer is already exist.")
            return render(request, 'add_customer.html')
        Customer.createcustomer(name = name, phone = phone, email = email)
        return redirect("customer_home")
    return render(request, 'add_customer.html')

def sort_customers(request):
    sort_by = request.GET.get('sort_by', 'Asc')
    customer = Customer.sortcustomerbyname(sort=sort_by)
    next_sort = 'Desc' if sort_by == 'Asc' else 'Asc'
    return render(request, 'display_customer.html', {'customers': customer, 'sort_by': sort_by, 'next_sort': next_sort})

def delete_customer(request, name, phone):
    Customer.objects.filter(name=name,phone=phone).delete()
    return redirect("customer_home")

def edit_customer(request, name, phone):
    customer = Customer.getcustomer(name=name,phone=phone)
    if request.method == 'POST':
        name = request.POST.get("Cname")
        phone = request.POST.get("Cphone")
        email = request.POST.get("Cemail")
        exit = Customer.objects.filter(name=name, phone=phone).exclude(name=customer.name, phone=customer.phone).first()
        if exit:
            messages.success(request, "Customer is already exist.")
            return render(request, 'edit_customer.html', {'customer': customer})
        customer.name = name
        customer.phone = phone
        customer.email = email
        customer.save()
        return redirect("customer_home")
    return render(request, 'edit_customer.html', {'customer': customer})

def search_customer(request):
    customer = request.GET.get("name", "").strip()
    customers = Customer.objects.annotate(
        normalized_name=Lower(Replace("name", Value(" "), Value("")))
    ).filter(
        normalized_name__icontains=customer
    )
    return render(request, 'display_customer.html', {'customers': customers, 'sort_by': 'Desc', 'next_sort': 'Asc'})

def customer_detail(request):
    customer = Order.objects.all().values('customer__name', 'customer__phone').annotate(order_count=Count('customer_id')).order_by('-order_count')
    return render(request, 'display_customer_orders.html', {'customer': customer})

def customer_orders(request, name, phone):
    customers = Order.objects.all().values('customer__name', 'customer__phone').annotate(order_count=Count('customer_id')).order_by('-order_count')
    customer = Customer.getcustomer(name=name, phone=phone)
    orders = Order.objects.filter(customer=customer)
    orders = orders.select_related('customer')
    orders = orders.prefetch_related('order_items__menu_item').order_by('created_at')
    for order in orders:
        for item in order.order_items.all():
            item.total_price = item.menu_item.price * item.quantity
        order.totalprice = sum(item.total_price for item in order.order_items.all())
    orders.customer_name = name
    orders.customer_phone = phone
    return render(request, 'display_customer_orders.html', {'orders': orders, 'customer': customers})

def search_customer_orders(request):
    customer = request.GET.get("name", "").strip()
    customers = (
        Order.objects
        .values('customer__name', 'customer__phone')
        .annotate(
            order_count=Count('customer_id'),
            normalized_name=Lower(Replace('customer__name', Value(" "), Value("")))
        )
        .filter(normalized_name__icontains=customer).order_by('-order_count')
    )
    return render(request, 'display_customer_orders.html', {'customer': customers})