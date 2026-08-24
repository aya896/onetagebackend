from django.urls import path

from .views import (
    BraceletListView,
    OwnedBraceletListView,
    OwnedBraceletCreateView,
)


urlpatterns = [
    path(
        "",
        BraceletListView.as_view(),
        name="bracelet-list",
    ),

    path(
        "owned/",
        OwnedBraceletListView.as_view(),
        name="owned-bracelets",
    ),

    path(
        "owned/create/",
        OwnedBraceletCreateView.as_view(),
        name="owned-bracelet-create",
    ),
]