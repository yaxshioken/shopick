from rest_framework.viewsets import ModelViewSet

from account.api_endpoints.account.serializers import (CardSerializer,
                                                       ProfileSerializer,
                                                       SellerSerializer,
                                                       TransactionSerializer,
                                                       UserSerializer)
from account.models import (Account, Card, Notifications, Profile, Seller,
                            Transaction)


class UserViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    my_tags=('Users',)

class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    my_tags=('Sellers   ',)

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    my_tags=('Card',)

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    my_tags=('Profiles',)

class NotificationsViewSet(ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = Notifications
    my_tags=('Notifications',)

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    my_tags=('Transactions',)