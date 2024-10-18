from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

from account.api_endpoints import LoginView, RegisterView
from shopick.api_endpoints import CommentViewSet, CategoryViewSet, ProductViewSet, WishlistViewSet, OrderViewSet

router = DefaultRouter()

router.register(r"comments", CommentViewSet, basename="comments"),
router.register(r"categories", CategoryViewSet, basename="categories"),

router.register(r"products", ProductViewSet, basename="products"),
router.register(r"wishlists", WishlistViewSet, basename="wishlists"),
router.register(r"orders", OrderViewSet , basename="orders"),


urlpatterns = router.urls
token_urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("api/token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
]
urlpatterns += token_urlpatterns