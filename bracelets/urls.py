from django.urls import path
from .views import (
    BraceletListCreateView,
    OwnedBraceletListView,
)


urlpatterns = [
    path("", BraceletListCreateView.as_view(), name="bracelet-list"),
    path("owned/", OwnedBraceletListView.as_view(), name="owned-bracelets"),
]