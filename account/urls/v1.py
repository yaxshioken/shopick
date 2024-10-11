from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainSlidingView,
                                            TokenRefreshSlidingView)

from account.api_endpoints import TransactionViewSet
from account.api_endpoints.account.views import (CardViewSet,
                                                 NotificationsViewSet,
                                                 ProfileViewSet, SellerViewSet,
                                                 UserViewSet)
from account.api_endpoints.auth.Login import LoginView
from account.api_endpoints.auth.Register import RegisterView

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users"),
router.register(r"profile", ProfileViewSet, basename="profile"),
router.register(r"sellers", SellerViewSet, basename="sellers"),
router.register(r"card", CardViewSet, basename="card"),
router.register(r"notifications", NotificationsViewSet, basename="notifications")
router.register(r"transactions", TransactionViewSet, basename="transactions")
urlpatterns = router.urls
token_urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("api/token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
]
urlpatterns += token_urlpatterns
