from rest_framework import serializers


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)

    def validate(self, data):
        if not data.get("email"):
            raise serializers.ValidationError("Emailingizni kiriting!!!")
        return data


class PasswordResetConfirmSerializer(serializers.Serializer):
    temporary_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")
        if new_password != confirm_password:
            raise serializers.ValidationError(
                "Parollar Bir-Biriga Mos Emas!!!"
            )
        return data


# class PasswordResetSmsRequestSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(required=True)
#
#     def validate_phone_number(self, value):
#         if not value.isdigit() or len(value) != 12:
#             raise serializers.ValidationError("Telefon raqami noto'g'ri.")
#         return value
