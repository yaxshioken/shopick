from contextvars import Token

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainSlidingView

from account.api_endpoints.auth.Register.serializers import RegisterSerializer
from shopick.models import Account


class RegisterView(TokenObtainSlidingView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    my_tags = ('Register',)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = [
    "RegisterView",
]
