import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.termcolors import RESET
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from account.choices import (NotificationChoice, PaymentStatusChoice,
                             PaymentTypeChoice)
from config.managers import UserManager
from shared.models import TimeStampedModel


class Account(AbstractUser, TimeStampedModel):
    is_active = models.BooleanField(default=False)
    phone = PhoneNumberField(unique=True, max_length=13, null=False)
    USERNAME_FIELD = "phone"
    objects = UserManager()
    is_seller=models.BooleanField(default=False)


    def __str__(self):
        return self.first_name


class Profile(TimeStampedModel):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    unique_together = ("user",)
    def __str__(self):
        return self.user


class Seller(TimeStampedModel):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="sellers"
    )
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    location = models.CharField(max_length=500)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Card(TimeStampedModel):
    card_number=models.CharField(max_length=16, unique=True,null=False)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3, null=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def clean(self):
        card = super().clean()
        if card.balance <= 0:
            raise ValidationError("Hisobingizdagi mablag' 0 dan kichik!!!")
        return card

    class Meta:
        unique_together = ("card_number", "user")

    def __str__(self):
        return self.card_number


class Notifications(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    message = models.TextField()
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="notifications"
    )
    is_read = models.BooleanField(default=False)
    type = models.CharField(choices=NotificationChoice.choices, max_length=15)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.message

    def mark_as_read(self):
        self.is_read = True
        self.save()



class Transaction(TimeStampedModel):
    card = models.CharField(max_length=16, blank=False, null=False)
    sender=models.CharField(max_length=40)   ##TODO
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    payment_type = models.CharField(
        max_length=200, choices=PaymentTypeChoice.choices, default=PaymentTypeChoice.UZS
    )
    payment_status = models.CharField(
        max_length=200, choices=PaymentStatusChoice.choices
    )

    def __str__(self):
        return f"{self.amount}"
