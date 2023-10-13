from django.shortcuts import redirect, render
from .models import Product
from django.http import JsonResponse


def get_product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)[:10]
    product_names = [product.name for product in products]
    
    # Check if there's an exact match for the query
    exact_match = Product.objects.filter(name__iexact=query).first()
    
    if exact_match:
        return redirect('products:product_details', pk=exact_match.pk)
    
    return JsonResponse(product_names, safe=False)


def product_details(request, product_id):
    # Assuming you have a Product model and retrieve the product by ID
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product_details.html', {'product': product})