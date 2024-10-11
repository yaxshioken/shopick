import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from account.choices import NotificationChoice
from config.managers import UserManager
from shared.models import TimeStampedModel


class Account(AbstractUser, TimeStampedModel):
    is_active = models.BooleanField(default=False)
    phone = PhoneNumberField(unique=True, max_length=13, null=False)
    USERNAME_FIELD = "phone"
    objects = UserManager()

    def __str__(self):
        return self.phone


class Profile(TimeStampedModel):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.user


class Seller(TimeStampedModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=500)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Card(TimeStampedModel):
    card_number = models.CharField(max_length=200)
    expiration_date = models.DateField(auto_now_add=True)
    card_token = models.CharField(max_length=200)
    cvv = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()
    payment_type = models.CharField(max_length=200)
    payment_date = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=200)

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
        self.is_read = False
        self.save()

    class Meta:
        verbose_name = "Notifications"
        verbose_name_plural = "Notifications"
