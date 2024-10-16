import random
import string

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.api_endpoints.auth.ResetParol.serializers import PasswordResetSerializer, PasswordResetConfirmSerializer
from account.models import Account


# from shared.task import generate_sms_code, send_sms



class PasswordResetRequestView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        Account = get_user_model()
        try:
            user = Account.objects.get(email=email)
            new_password = self.generate_random_password()
            user.set_password(new_password)
            user.profile.temporary_password = new_password
            user.save()
            user.profile.save()
            send_mail(
                "<h1>Parolni tiklash</h1>",
                f"<b>Sizning yangi parolingiz</b>: {new_password}",
                "Account",
                [user.email],
                fail_silently=False,
            )
            return Response(
                {"message": "Tasdiqlash kodi emailga yuborildi."},
                status=status.HTTP_200_OK,
            )
        except Account.DoesNotExist:
            return Response(
                {"error": "Email topilmadi."}, status=status.HTTP_404_NOT_FOUND
            )

    def generate_random_password(self, length=6):
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for i in range(length))


class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [AllowAny]
    my_tags = ('ResetPassword',)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        temporary_password = serializer.validated_data["temporary_password"]
        new_password = serializer.validated_data["new_password"]

        try:
            user = Account.objects.get(profile__temporary_password=temporary_password)
            user.set_password(new_password)
            user.profile.temporary_password = None
            user.save()
            return Response(
                {"message": "Parol muvaffaqiyatli o'zgartirildi."},
                status=status.HTTP_200_OK,
            )
        except Account.DoesNotExist:
            return Response(
                {"error": "Vaqtinchalik parol noto'g'ri."},
                status=status.HTTP_400_BAD_REQUEST,
            )


# class PasswordResetSmsRequestView(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = PasswordResetSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         phone_number = serializer.validated_data['phone_number']
#         Account = get_user_model()
#
#         try:
#             user = Account.objects.get(phone_number=phone_number)
#             sms_code = generate_sms_code()
#             send_sms(user.phone_number, sms_code)
#             return Response({"message": "SMS kodi yuborildi."}, status=status.HTTP_200_OK)
#         except Account.DoesNotExist:
#             return Response({"error": "Telefon raqam topilmadi."}, status=status.HTTP_404_NOT_FOUND)
