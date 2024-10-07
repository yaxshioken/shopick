from django.urls import path
from rest_framework.routers import DefaultRouter

from shopick import api_endpoints
from shopick.api_endpoints.account.views import (CardViewSet, CommentViewSet,
                                                 NotificationsViewSet,
                                                 ProfileViewSet, SellerViewSet,
                                                 UserViewSet, WishlistViewSet)
from shopick.api_endpoints.shopick.views import (CategoryViewSet, OrderViewSet,
                                                 ProductViewSet)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users"),
router.register(r"profile", ProfileViewSet, basename="profile"),
router.register(r"comments", CommentViewSet, basename="comments"),
router.register(r"categories", CategoryViewSet, basename="categories"),
router.register(r"sellers", SellerViewSet, basename="sellers"),
router.register(r"products", ProductViewSet, basename="products"),
router.register(r"wishlists", WishlistViewSet, basename="wishlists"),
router.register(r"orders", OrderViewSet, basename="orders"),
router.register(r"card", CardViewSet, basename="card"),

router.register(r"notifications", NotificationsViewSet, basename="notifications")
urlpatterns = router.urls

from rest_framework_simplejwt.views import (TokenObtainSlidingView,
                                            TokenRefreshSlidingView)

token_urlpatterns = [
    path("login/", api_endpoints.LoginView.as_view(), name="login"),
    path("register/", api_endpoints.RegisterView.as_view(), name="register"),
    path("api/token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
]
urlpatterns += token_urlpatterns
