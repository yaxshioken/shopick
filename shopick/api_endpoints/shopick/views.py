from rest_framework import viewsets

from shopick.api_endpoints.shopick.serializers import (CategorySerializer,
                                                       OrderSerializer,
                                                       ProductSerializer)
from shopick.models import Category, Order, Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
