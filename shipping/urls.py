from rest_framework.routers import DefaultRouter
from .views import ShippingViewSet

router = DefaultRouter()
router.register("", ShippingViewSet)

urlpatterns = router.urls