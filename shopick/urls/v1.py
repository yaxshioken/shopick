from rest_framework.routers import DefaultRouter
from shopick.api_endpoints.shopick.views import (CategoryViewSet,
                                                 CommentViewSet, OrderViewSet,
                                                 ProductViewSet,
                                                 WishlistViewSet)

router = DefaultRouter()

router.register(r"comments", CommentViewSet, basename="comments"),
router.register(r"categories", CategoryViewSet, basename="categories"),

router.register(r"products", ProductViewSet, basename="products"),
router.register(r"wishlists", WishlistViewSet, basename="wishlists"),
router.register(r"orders", OrderViewSet, basename="orders"),

urlpatterns = router.urls
