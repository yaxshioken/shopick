from rest_framework import serializers

from shopick.models import Order, Card, Wishlist, Product, Seller, Category, Comment, Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone")
        extra_kwargs = {
            "first_name": {"required": True},
            "email": {"required": True},
            "phone": {"required": True},
            "username": {"required": False},
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', "user", "address", "city", "country")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', "user", "comment")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', "name",)


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("user", "name", "description", "location", "phone_number")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = (
        #     "name",
        #     "description",
        #     "amount",
        #     "price",
        #     "price",
        #     "size",
        #     "seller",
        #     "color",
        #     "discount_percent",
        #     "brand",
        #     "like",
        #     "views",
        # )
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("product", "user", "quantity")


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            "card_number",
            "expiration_date",
            'card_token',
            "cvv",
            "payment_amount",
            "payment_type",
            "payment_date",
            "payment_status"
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'reception_area',
            'user_area',
            'user',
            'payment_type',
            'product',
            'amount',
            'order_date',
            'delivery_date',
            'status'
        )
