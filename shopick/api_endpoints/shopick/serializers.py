from rest_framework import serializers

from shopick.models import Category, Comment, Order, Product, Wishlist
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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # extra_kwargs = {
        #     "like":{"required":False},
        #     "product":{"required":False},
        #
        # }
        read_only_fields = ("user",)


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
