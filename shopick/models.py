import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from account.models import Account
from shared.models import TimeStampedModel
from shopick.choices import ColorChoice, SizeChoice


class Category(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Comment(TimeStampedModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
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
    like = models.ManyToManyField(Account, related_name="product_like", blank=True)
    views = models.ManyToManyField(Account, related_name="viewed_products", blank=True)
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
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)


class Order(TimeStampedModel):
    reception_area = models.CharField(max_length=200)
    user_area = models.CharField(max_length=200)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200)

    def __str__(self):
        return str(self.product)
