from django.db import models

# Create your models here.
from django.db import models
from User_Profile.models import Profile
from Products.models import Product

class Cart(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, null=True, blank=True, related_name='cart_user')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    is_guest = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def subtotal(self):
        return self.quantity * self.product.price

class GuestUser(models.Model):
    cart = models.OneToOneField('Cart', on_delete=models.CASCADE, related_name='guest_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  