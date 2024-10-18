from rest_framework import serializers


from shopick.models import ( Category, Comment, Order, Product,
                            Seller,  Wishlist)



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "user", "comment")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


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
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("product", "user", "quantity")




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "reception_area",
            "user_area",
            "user",
            "payment_type",
            "product",
            "amount",
            "order_date",
            "delivery_date",
            "status",
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'comment', 'parent', 'like']

    def validate(self, data):
        product = data.get('product')
        user = data.get('user')
        return data