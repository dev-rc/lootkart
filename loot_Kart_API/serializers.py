# products/serializers.py
from rest_framework import serializers
from Products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
