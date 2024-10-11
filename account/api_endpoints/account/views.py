from rest_framework.viewsets import ModelViewSet

from account.api_endpoints.account.serializers import (CardSerializer,
                                                       ProfileSerializer,
                                                       SellerSerializer,
                                                       UserSerializer)
from account.models import Account, Card, Notifications, Profile, Seller


class UserViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class NotificationsViewSet(ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = Notifications
