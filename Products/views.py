from django.shortcuts import redirect, render
from .models import Product
from django.http import JsonResponse


def get_product_list(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


def search_products(request):
    query = request.GET.get("q","")
 
    products = Product.objects.filter(name__icontains=query)[:10]
    product_names = [product.name for product in products]

    # Check if there's an exact match for the query
    exact_match = Product.objects.filter(name__iexact=query).first()

    if exact_match:
        return redirect("products:product_details", pk=exact_match.pk)

    return JsonResponse(product_names, safe=False)

def product_search(request):
    product_name = request.GET.get('product')
    search_results = []

    if product_name:
        # Perform the search if a product_name is provided
        search_results = Product.objects.filter(name__icontains=product_name)

    return render(request, 'products/search_results.html', {'products': search_results, 'search_query': product_name})



def product_details(request, product_name, product_id):
    try:
        product = Product.objects.get(id=product_id, name=product_name)
    except Product.DoesNotExist:
        print(product_id)
        pass

    # # Assuming you have a Product model and retrieve the product by ID
    # product = Product.objects.get(id=request.GET.get("id"))
    # print(product.id)
    return render(request, 'products/product_details.html', {'product': product})
