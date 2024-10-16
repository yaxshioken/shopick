from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from account.models import Transaction
from shopick import api_endpoints
from shopick.api_endpoints.auth.ResetParol.view import PasswordResetRequestView
from shopick.views import (CategoryViewSet, CommentViewSet, ProductViewSet, UserViewSet,
                           ProfileViewSet, SellerViewSet, WishlistViewSet, OrderViewSet, CardViewSet)

router = DefaultRouter()

router.register(r"comments", CommentViewSet, basename="comments"),
router.register(r"categories", CategoryViewSet, basename="categories"),

router.register(r"products", ProductViewSet, basename="products"),
router.register(r"wishlists", WishlistViewSet, basename="wishlists"),
router.register(r"orders", OrderViewSet, basename="orders"),
router.register("payments", Transaction, basename="payments"),

urlpatterns = router.urls
