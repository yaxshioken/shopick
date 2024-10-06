from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
import random
import string

from shopick.api_endpoints.auth.ResetParol.serializers import PasswordResetSerializer


class PasswordResetRequestView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            new_password = self.generate_random_password()
            user.set_password(new_password)
            user.save()
            send_mail(
                'Parolni tiklash',
                f'Sizning yangi parolingiz: {new_password}',
                'User',
                [user.email],
                fail_silently=False,
            )
            return Response({"message": "Yangi parol emailga yuborildi."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Email topilmadi."}, status=status.HTTP_404_NOT_FOUND)

    def generate_random_password(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))
