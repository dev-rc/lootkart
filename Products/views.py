from django.shortcuts import render
from .models import Product
from django.http import JsonResponse


def get_product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)[:10]  # Adjust as needed
    product_names = [product.name for product in products]
    return JsonResponse(product_names, safe=False)