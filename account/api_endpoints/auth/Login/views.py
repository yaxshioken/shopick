from rest_framework_simplejwt.views import TokenObtainSlidingView

from account.api_endpoints.auth.Login.serializers import LoginSerializer


class LoginView(TokenObtainSlidingView):
    serializer_class = LoginSerializer
    my_tags = ('Login',)

__all__ = ["LoginView"]
