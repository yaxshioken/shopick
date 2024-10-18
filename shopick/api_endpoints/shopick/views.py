from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from shopick.api_endpoints.shopick.serializers import (CategorySerializer,
                                                       CommentSerializer,
                                                       OrderSerializer,
                                                       ProductSerializer,
                                                       WishlistSerializer)
from shopick.models import Category, Comment, Order, Product, Wishlist, Like


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

from django.core.mail import send_mail

class CommentView(APIView):
    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        comment_data = request.data
        parent_comment = None

        if 'parent' in comment_data:
            try:
                parent_comment = Comment.objects.get(id=comment_data['parent'])
            except Comment.DoesNotExist:
                return Response({"detail": "Parent comment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=comment_data)
        if serializer.is_valid():
            comment = serializer.save(user=request.user, product=product, parent=parent_comment)

            if product.user.email:
                send_mail(
                    'Yangi izoh keldi',
                    f'Sizning {product.name} mahsulotingizga yangi izoh keldi: {comment.comment}',
                    'from@example.com',
                    [product.user.email],
                    fail_silently=False,
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LikeView(APIView):
    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        if product.user == request.user:
            return Response({"detail": "You cannot like your own product."}, status=status.HTTP_400_BAD_REQUEST)

        if not Like.objects.filter(user=request.user, product=product).exists():
            like = Like.objects.create(user=request.user, product=product)
            return Response({"detail": "Liked successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You have already liked this product."}, status=status.HTTP_400_BAD_REQUEST)