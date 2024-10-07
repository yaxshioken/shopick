from bisect import insort

from rest_framework import serializers

from shopick.models import Category, Order, Product
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
