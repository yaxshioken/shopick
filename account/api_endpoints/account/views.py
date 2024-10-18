from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from account.api_endpoints.account.serializers import (CardSerializer,
                                                       ProfileSerializer,
                                                       SellerSerializer,
                                                       TransactionSerializer,
                                                       UserSerializer, NotificationsSerializer)
from account.models import (Account, Card, Notifications, Profile, Seller,
                            Transaction)


class UserViewSet(ModelViewSet):
    queryset = Account.objects.all().order_by('id')
    serializer_class = UserSerializer
    my_tags=('Users',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['id','phone','email','first_name','last_name','created_at','updated_at']



class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all().order_by('id')
    serializer_class = SellerSerializer
    my_tags=('Sellers',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['id','name','location','phone_number','user','created_at','updated_at']


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer
    my_tags=('Card',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['id','card_number','expiration_date','cvv','user','balance','created_at','updated_at']

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    my_tags=('Profiles',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['id','user','address','city','country','created_at','updated_at']

class NotificationsViewSet(ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    my_tags=('Notifications',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['id','account','type','created_at','updated_at']

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    my_tags=('Transactions',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['id','card','sender','receiver','payment_status','created_at','updated_at']