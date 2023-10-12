
from Products.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.
class ProductAPIView(APIView):
    def get(self, request):
        # Retrieve the products (e.g., from a model)
        products = Product.objects.all()

        # Serialize the products to JSON
        serialized_products = ProductSerializer(products, many=True)

        return Response(serialized_products.data)