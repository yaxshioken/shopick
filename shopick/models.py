import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from config.managers import UserManager
from shared.models import TimeStampedModel
from shopick.choices import ColorChoice, NotificationChoice, SizeChoice


class User(AbstractUser, TimeStampedModel):
    is_active = models.BooleanField(default=False)
    phone = PhoneNumberField(unique=True, max_length=13, null=False)
    USERNAME_FIELD = "phone"
    objects = UserManager()
    def __str__(self):
        return self.phone


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.user


class Category(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Seller(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=500)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.comment


class Product(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    amount = models.IntegerField(null=False)
    picture = models.ImageField(upload_to="products/", null=True, blank=True)
    price = models.IntegerField(null=False)
    size = models.CharField(choices=SizeChoice.choices, default=SizeChoice.NONE)
    color = models.CharField(choices=ColorChoice.choices, default=ColorChoice.NONE)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    brand = models.CharField(max_length=200)
    like = models.ManyToManyField(User, related_name="product_like", blank=True)
    views = models.ManyToManyField(User, related_name="viewed_products", blank=True)
    category = models.ManyToManyField(Category, related_name="categories")

    def total_views(self):
        return self.views.count()

    def calculate_discount(self):
        return self.price * (self.discount_percent / 100)

    def final_price(self):
        return self.price - self.calculate_discount()

    def __str__(self):
        return self.name

    @property
    def build_url(self):
        return f"/products/{self.id}"


class Wishlist(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)


class Order(TimeStampedModel):
    reception_area = models.CharField(max_length=200)
    user_area = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200)

    def __str__(self):
        return str(self.product)


class Card(TimeStampedModel):
    card_number = models.CharField(max_length=200)
    expiration_date = models.DateField(auto_now_add=True)
    card_token = models.CharField(max_length=200)
    cvv = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        User, on_delete=models.CASCADE, related_name="notifications"
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
