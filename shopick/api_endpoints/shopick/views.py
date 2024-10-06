from rest_framework import viewsets

from shopick.api_endpoints.shopick.serializers import ProductSerializer, OrderSerializer, CategorySerializer
from shopick.models import Product, Order, Category


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
