from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainSlidingView,
                                            TokenRefreshSlidingView)

from account.api_endpoints import (PasswordResetConfirmView,
                                   PasswordResetRequestView,
                                   TransactionViewSet, LoginView, RegisterView)
from account.api_endpoints.account.views import (CardViewSet,
                                                 NotificationsViewSet,
                                                 ProfileViewSet, SellerViewSet,
                                                 UserViewSet)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users"),
router.register(r"profile", ProfileViewSet, basename="profile"),
router.register(r"sellers", SellerViewSet, basename="sellers"),
router.register(r"card", CardViewSet, basename="card"),
router.register(r"notifications", NotificationsViewSet, basename="notifications")
router.register(r"transactions", TransactionViewSet, basename="transactions")

urlpatterns = router.urls
token_urlpatterns = [
    path(
        "password-reset-request/",
        PasswordResetRequestView.as_view(),
        name="password_reset_request",
    ),
    path(
        "password-reset-confirm/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
]

urlpatterns += token_urlpatterns


