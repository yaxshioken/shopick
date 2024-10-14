from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework_simplejwt.serializers import (PasswordField, TokenObtainPairSerializer)


class LoginSerializer(TokenObtainPairSerializer):
    phone = PhoneNumberField(write_only=True)
    password = PasswordField(write_only=True)
    extra_kwargs = {
        "username": {
            "required": False,
            "blank": True,
        },
    }
