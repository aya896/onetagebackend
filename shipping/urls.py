from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ShippingViewSet


router = DefaultRouter()

router.register(
    "",
    ShippingViewSet,
    basename="shipping",
)

urlpatterns = router.urls