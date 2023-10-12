from django.shortcuts import render
from django.shortcuts import render
from .models import Product
def suggest_products_name(request):
    products = Product.objects.values_list('name', flat=True)
    return render(request, 'base.html', {'products': list(products)})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


