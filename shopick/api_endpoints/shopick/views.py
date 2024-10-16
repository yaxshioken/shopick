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