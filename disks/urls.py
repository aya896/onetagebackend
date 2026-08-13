from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiskViewSet

router = DefaultRouter()
router.register("", DiskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]