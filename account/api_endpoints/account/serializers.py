from django.utils import timezone
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import transaction
from account.choices import PaymentStatusChoice
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
        fields = ('id', 'name', 'description', 'location', 'phone_number')
        read_only_fields = ('id', "created_at", "updated_at", 'user')
        extra_kwargs = {
            "user": {"required": False},
        }


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
            "card_number": {"required": True},
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
        read_only_fields = ("user",)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)

    def validate(self, data):
        return data

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return super().get_serializer(*args, **kwargs)









class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "card",
            "amount",
            "payment_status",
            "sender",
        )
        extra_kwargs = {
            "payment_type": {"write_only": True},
            "payment_status": {"read_only": True},
            "sender": {"read_only": True},
        }

    def validate(self, data):
        user = self.context["request"].user
        card_owner = get_object_or_404(Card, user=user)
        receiver_card_number = data.get("card")


        if not Card.objects.filter(user=user).exists():
            raise serializers.ValidationError('Sizda aktiv kartalar mavjud emas :)')


        if receiver_card_number is None:
            raise serializers.ValidationError("Siz kiritgan karta mavjud emas :)")

        receiver_card = get_object_or_404(Card, card_number=receiver_card_number)


        amount = data.get("amount")
        if amount is None or amount <= 0:
            raise serializers.ValidationError("Mablag' miqdori to'g'ri kiritilmagan!")


        if card_owner.balance < amount:
            raise serializers.ValidationError("Hisobingizda mablag' yetarli emas!!!")


        card_owner.balance -= amount
        receiver_card.balance += amount


        data['sender'] = user
        data['payment_status'] = PaymentStatusChoice.SUCCESS


        with transaction.atomic():
            card_owner.save()
            receiver_card.save()

        return data

    def create(self, validated_data):
        # user = self.context["request"].user
        transaction = Transaction.objects.create(**validated_data)
        return transaction