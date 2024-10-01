from fcntl import FASYNC

from rest_framework import serializers

from shopick.models import Category, Comment, Product, Profile, Seller, User


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
        fields = ("user", "address", "city", "country", "postal_code")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "comment")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("user", "name", "description", "location", "phone_number")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "amount",
            "price",
            "price",
            "size",
            "category",
            "seller",
            "color",
            "discount_percent",
            "brand",
            "like",
            "views",
        )
