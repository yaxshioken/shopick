from django.db.models.query_utils import Q
from rest_framework.viewsets import ModelViewSet

from shopick.api_endpoints.shopick.serializers import (CategorySerializer,
                                                       CommentSerializer,
                                                       OrderSerializer,
                                                       ProductSerializer,
                                                       WishlistSerializer)
from shopick.models import Category, Comment, Order, Product, Wishlist


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    my_tags = ('Products',)

    def get_queryset(self):
        query = self.request.query_params.get("search", None)
        queryset = super().get_queryset()
        name = self.request.query_params.get("name", None)
        description = self.request.query_params.get("description", None)
        amount = int(self.request.query_params.get("amount", 0))
        price=self.request.query_params.get("price", None)
        size=self.request.query_params.get("size", None)
        color=self.request.query_params.get("color", None)
        discount=self.request.query_params.get("discount", None)
        brand=self.request.query_params.get("brand", None)
        category=self.request.query_params.get("category", None)

        if name:
            return queryset.filter(name__icontains=name)
        if description:
            return queryset.filter(description__icontains=description)
        if amount:
            return queryset.filter(amount=amount)
        if query:
            queryset = queryset.filter(
                Q(body__icontains=query) | Q(title__icontains=query)
            )

        return queryset

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    my_tags=('Orders',)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    my_tags = ('Categories',)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    my_tags=('Comments',)

class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    my_tags=('Wishlists',)