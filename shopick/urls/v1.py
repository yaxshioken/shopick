
from rest_framework.routers import DefaultRouter

from account.models import Transaction
from shopick.api_endpoints import CommentViewSet, CategoryViewSet, ProductViewSet, WishlistViewSet, OrderViewSet

router = DefaultRouter()

router.register(r"comments", CommentViewSet, basename="comments"),
router.register(r"categories", CategoryViewSet, basename="categories"),

router.register(r"products", ProductViewSet, basename="products"),
router.register(r"wishlists", WishlistViewSet, basename="wishlists"),
router.register(r"orders", OrderViewSet , basename="orders"),


urlpatterns = router.urls
