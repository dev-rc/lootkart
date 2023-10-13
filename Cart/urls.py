from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('view/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-guest/', views.view_cart_guest, name='view_cart_guest'),
    path('add-guest/<int:product_id>/', views.add_to_cart_guest, name='add_to_cart_guest'),
]
