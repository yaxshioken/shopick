from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from shared.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    is_active = models.BooleanField(default=False)
    phone = PhoneNumberField(unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", "email"]


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # postal_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


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


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='Product_comment')
    like = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    picture = models.ImageField(upload_to="products/")
    price = models.IntegerField()
    size = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.CharField(max_length=200)
    like = models.ManyToManyField(User, related_name="product_like", blank=True)
    views = models.ManyToManyField(User, related_name="viewed_products", blank=True)

    def total_views(self):
        return self.views.count()

    def calculate_discount(self):
        return self.price * (self.discount_percent / 100)

    def final_price(self):
        return self.price - self.calculate_discount()

    def __str__(self):
        return self.name


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
