from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from rest_framework import serializers

from shopick.models import Category,  Order, Product, Wishlist
from shopick.tasks import create_notification_for_users


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "picture": {"required": False, "allow_null": True},
        }

    @receiver(post_save, sender=Product)
    def notify_users(sender, instance, created, **kwargs):
        if created:
            create_notification_for_users.delay(instance.id)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1





class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
