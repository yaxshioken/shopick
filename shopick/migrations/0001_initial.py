# Generated by Django 5.1.2 on 2024-10-11 16:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField()),
                ("amount", models.IntegerField()),
                (
                    "picture",
                    models.ImageField(blank=True, null=True, upload_to="products/"),
                ),
                ("price", models.IntegerField()),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("", "None"),
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("large", "Large"),
                        ],
                        default="",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("", "None"),
                            ("red", "Red"),
                            ("green", "Green"),
                            ("yellow", "Yellow"),
                            ("blue", "Blue"),
                            ("purple", "Purple"),
                            ("pink", "Pink"),
                            ("white", "White"),
                            ("black", "Black"),
                        ],
                        default="",
                    ),
                ),
                (
                    "discount_percent",
                    models.DecimalField(decimal_places=2, max_digits=5, null=True),
                ),
                ("brand", models.CharField(max_length=200)),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="categories", to="shopick.category"
                    ),
                ),
                (
                    "like",
                    models.ManyToManyField(
                        blank=True,
                        related_name="product_like",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "views",
                    models.ManyToManyField(
                        blank=True,
                        related_name="viewed_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("reception_area", models.CharField(max_length=200)),
                ("user_area", models.CharField(max_length=200)),
                ("payment_type", models.CharField(max_length=200)),
                ("amount", models.IntegerField()),
                ("order_date", models.DateField(auto_now_add=True)),
                ("delivery_date", models.DateField(auto_now_add=True)),
                ("status", models.CharField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shopick.product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("like", models.IntegerField(default=0)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shopick.product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("quantity", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shopick.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
