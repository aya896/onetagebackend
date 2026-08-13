from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BeadViewSet

router = DefaultRouter()
router.register(r"", BeadViewSet)

urlpatterns = [
    path("", include(router.urls)),
]