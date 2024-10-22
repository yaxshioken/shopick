from django.contrib.auth.decorators import permission_required
from psutil import users
from rest_framework.response import Response
from rest_framework import viewsets, status, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from account.api_endpoints.account.serializers import (CardSerializer,
                                                       NotificationSerializer,
                                                       ProfileSerializer,
                                                       SellerSerializer,
                                                       TransactionSerializer,
                                                       UserSerializer)
from account.models import (Account, Card, Notifications, Profile, Seller,
                            Transaction)


class UserViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    my_tags = ("Users",)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    my_tags = ("Sellers",)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user:
            data = request.data.copy()
            data['user'] = user
            seller = Seller.objects.create(**data)
            serializer = SellerSerializer(seller)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    my_tags = ("Card",)

    def list(self, request, *args, **kwargs):
        user = request.user
        cards = self.queryset.filter(user=user)

        if cards.exists():
            serializer = CardSerializer(cards, many=True).data
            return Response(serializer)
        else:
            return Response({"message": "Sizda aktiv kartalar mavjud emas!"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        card = Card.objects.filter(user=request.user)
        if card.filter(pk=kwargs.get('pk')).exists():
            card.get(pk=kwargs.get('pk')).delete()
            return Response({'message': "Muvafaqiyatli o'chirildi!!!"}, status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    my_tags = ("Profiles",)

    @permission_required("account.add_profile ")
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def list(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        data = ProfileSerializer(profile).data
        return Response(data)

    def update(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        serializer = self.serializer_class(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        profile.delete()
        return Response({"success": "Muvaffaqiyatli o'chirildi!"}, status=204)


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    my_tags = ('Notifications',)
    @permission_required("account.add_notifications",)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @permission_required("account.change_notifications",)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user=request.user
        notifications=self.queryset.filter(account=user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        notification = self.queryset.filter(account=user, pk=kwargs.get('pk')).first()

        if notification:
            notification.delete()
            return Response({"message": "Muvaffaqiyatli o'chirildi!"}, status=204)
        else:
            return Response({"message": "Bunday bildirishnoma topilmadi!"}, status=404)


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    my_tags = ("Transactions",)


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @permission_required("account.delete_transaction")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
