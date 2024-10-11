from rest_framework_simplejwt.views import TokenObtainSlidingView

from account.api_endpoints.auth.Login.serializers import LoginSerializer


class LoginView(TokenObtainSlidingView):
    serializer_class = LoginSerializer


__all__ = ["LoginView"]
