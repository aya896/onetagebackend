from django.urls import path

from .views import (
    ActivateBraceletView,
    NFCProfileDetailView,
    ScanBraceletView,
)

urlpatterns = [

    path(
        "activate/",
        ActivateBraceletView.as_view(),
        name="activate-bracelet"
    ),

    path(
        "profile/<int:bracelet_id>/",
        NFCProfileDetailView.as_view(),
        name="profile"
    ),

    path(
        "scan/<str:uid>/",
        ScanBraceletView.as_view(),
        name="scan"
    ),

]