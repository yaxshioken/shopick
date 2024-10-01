from uuid import uuid4

from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from shopick.models import User


class RegisterSerializer(TokenObtainPairSerializer):
    first_name = CharField(required=True)
    last_name = CharField(required=False)
    email = EmailField(required=True)
    password = CharField(required=True, min_length=8, max_length=128, write_only=True)
    password2 = CharField(required=True, min_length=8, max_length=128, write_only=True)
    phone = PhoneNumberField(required=True)

    class Meta:
        model = User
        extra_kwargs = {
            "last_name": {"required": False, "allow_blank": True},
            "username": {"required": False, "allow_blank": True},
        }

    def validate(self, data):
        password = data.get("password")
        password2 = data.get("password2")
        phone = data.get("phone")
        email = data.get("email")

        if password != password2:
            raise ValidationError({"password": _("Passwords must match.")})

        if User.objects.filter(phone=phone).exists():
            raise ValidationError({"phone": _("Phone number already exists.")})

        if User.objects.filter(email=email).exists():
            raise ValidationError({"email": _("Email already exists.")})

        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        phone = validated_data.get("phone")

        username = slugify(f"{uuid4()}-{phone}")
        while User.objects.filter(username=username).exists():
            username = slugify(f"{uuid4()}-{phone}")

        user = User.objects.create(**validated_data, username=username)
        user.set_password(password)
        user.save()

        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": str(user.phone),
            "username": user.username,
        }
