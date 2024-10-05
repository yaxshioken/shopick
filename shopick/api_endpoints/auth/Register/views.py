from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainSlidingView

from shopick.api_endpoints.auth.Register.serializers import RegisterSerializer


class RegisterView(TokenObtainSlidingView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save user

__all__ = ["RegisterView"]
