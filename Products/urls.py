from django.urls import path
from . import views



app_name = 'products'

urlpatterns = [
    path('', views.get_product_list, name='products'),
    path('search/', views.search_products, name='search_products'),
    path('products/search/', views.product_search, name='product_search'),
    path('<str:product_name>/<int:product_id>/', views.product_details, name='product_details'),




]
