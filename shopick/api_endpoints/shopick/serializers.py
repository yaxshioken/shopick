from rest_framework import serializers

from shopick.models import Category, Comment, Order, Product, Wishlist, Like


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
        fields = ['user', 'product', 'comment', 'parent', 'like']

    def validate(self, data):
        product = data.get('product')
        user = data.get('user')
        return data

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'product', 'comment', 'parent', 'like', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'product', 'liked_at']