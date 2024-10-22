from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

from shopick.api_endpoints import (
    CategoryViewSet,
    CommentaryViewSet,
    OrderViewSet,
    ProductViewSet,
    WishlistViewSet,
    CommentView,
    LikeView,
)

router = DefaultRouter()
router.register(r"comments", CommentaryViewSet, basename="comments")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"wishlists", WishlistViewSet, basename="wishlists")
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
    path('', include(router.urls)),
    path("api/token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
    path("products/comments/", CommentView.as_view(), name="product_comments"),
    path("products/like/", LikeView.as_view(), name="product_like"),
]
