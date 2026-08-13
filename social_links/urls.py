from django.urls import path

from .views import (
    SocialLinkListCreateView,
    SocialLinkDetailView,
)

urlpatterns = [

    path(
        "",
        SocialLinkListCreateView.as_view(),
    ),

    path(
        "<int:pk>/",
        SocialLinkDetailView.as_view(),
    ),

]