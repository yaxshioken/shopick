from django.urls import path
from rest_framework import routers

from shopick import api_endpoints
from shopick.views import (CategoryViewSet, CommentViewSet, ProductViewSet,
                           ProfileViewSet, SellerViewSet, UserViewSet)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"comments", CommentViewSet, basename="comments")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"sellers", SellerViewSet, basename="sellers")
router.register(r"products", ProductViewSet, basename="products")

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
