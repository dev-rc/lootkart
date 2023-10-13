from django.shortcuts import redirect, render
from Products.models import Product
from .models import Cart, CartItem

def view_cart(request):
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.subtotal() for item in cart_items)
    
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    cart = request.user.cart
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    
    return redirect('cart:view_cart')
def add_to_cart_guest(request, product_id):
    cart, created = Cart.objects.get_or_create(is_guest=True)
    guest_user, created = GuestUser.objects.get_or_create(cart=cart)
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart_guest')

def view_cart_guest(request):
    cart = Cart.objects.filter(is_guest=True).first()
    if not cart:
        return render(request, 'cart/empty_cart_guest.html')
    guest_user = cart.guest_user
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart/view_cart_guest.html', {'cart_items': cart_items, 'total_price': total_price, 'guest_user': guest_user})
