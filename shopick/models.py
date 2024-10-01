from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from pkg_resources import require

from shared.apps import SharedConfig
from shared.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    first_name = models.CharField(
        max_length=200,
    )
    last_name = models.CharField(
        max_length=200,
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = PhoneNumberField(
        unique=True,
        blank=False,
        null=False,
    )
    is_active=models.BooleanField(default=False)


    USERNAME_FIELD = "phone"


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Seller(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=500)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    picture = models.ImageField(upload_to="products/")
    price = models.IntegerField()
    size = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.CharField(max_length=200)
    like = models.ManyToManyField(User, related_name="product_like", blank=True)
    comment = models.ManyToManyField(
        Comment, related_name="product_comment", blank=True
    )
    views = models.ManyToManyField(User, related_name="viewed_products", blank=True)
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="seller_products"
    )

    def total_views(self):
        return self.views.count()

    def calculate_discount(self):

        return self.price * (self.discount_percent / 100)

    def final_price(self):
        return self.price - self.calculate_discount()

    def __str__(self):
        return self.name
