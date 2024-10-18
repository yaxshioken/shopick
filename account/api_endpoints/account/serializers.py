from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from account.models import (Account, Card, Notifications, Profile, Seller,
                            Transaction)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "phone", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True},
        }


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            "id",
            "card_number",
            "expiration_date",
            "cvv",
            "balance",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "cvv": {"write_only": True, "required": True},
            "card_number": {"write_only": True, "required": True},
            "expiration_date": {"write_only": True, "required": True},
            "balance": {"required": True},
        }

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)

    def validate(self, data):
        if (
            data["card_number"] is not None
            and data["expiration_date"] >= timezone.now().date()
        ):
            raise serializers.ValidationError(
                "Karta raqami noto'g'ri yoki muddati o'tgan."
            )
        elif data.get("balance", 0) <= 0:
            raise serializers.ValidationError("Hisobingizda mablag' yetarli emas!!!")
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class NotificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = '__all__'

from rest_framework import serializers
from django.shortcuts import get_object_or_404


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "card",
            "amount",
            "payment_amount",
            "payment_status",
        )
        extra_kwargs = {
            "payment_type": {"write_only": True},
            "payment_amount": {"required": True},
            "payment_status": {"read_only": True},
            "cvv": {"required": False, "write_only": True},
        }

    def validate(self, data):
        user = self.context["request"].user
        card_owner = get_object_or_404(Card, user=user)
        receiver_card_number = data.get("card_number")

        if not card_owner.card_number or card_owner.card_number == receiver_card_number:
            raise serializers.ValidationError("Biron nima xato ketdi Tekshiring !!!")
        elif card_owner.card_number < data["payment_amount"]:
            raise serializers.ValidationError("Hisobingizda mablag' yetarli emas!!!")
        elif receiver_card_number is None:
            raise serializers.ValidationError("Siz kiritgan karta mavjud emas :)")

        return data

    def create(self, validated_data):
        user = self.context["request"].user
        card = get_object_or_404(Card, user=user)
        validated_data["card"] = card.card_number

        receiver = self.context.get("receiver")
        if receiver:
            validated_data["receiver"] = receiver.card_number

        return super().create(validated_data)
