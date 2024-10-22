

from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from shopick.models import Category, Comment, Like, Order, Product, Wishlist
from shopick.tasks import create_notification_for_users


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "picture": {"required": False, "allow_null": True},
        }

    def create(self, validated_data):
        instance = super().create(validated_data)
        create_notification_for_users.delay(instance.id)
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1

        ##TODO user category yaratganda admin uni tasdiqlashi kerak

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"
#         # extra_kwargs = {
#         #     "like":{"required":False},
#         #     "product":{"required":False},
#         #
#         # }
#         read_only_fields = ("user",)
#

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "product", "comment", "parent", "like"]
        extra_kwargs = {"user": {"read_only": True}}

    def validate(self, attrs):
        get_object_or_404(Product, pk=attrs["product"])
        return attrs

    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        return super().create(validated_data)



class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"




class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["user", "product", "liked_at"]
