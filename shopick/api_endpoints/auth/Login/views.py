from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenObtainSlidingView)

from shopick.api_endpoints.auth.Login.serializers import LoginSerializer


class LoginView(TokenObtainSlidingView):
    serializer_class = LoginSerializer


__all__ = ["LoginView"]
