from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)



urlpatterns = [

    path("admin/", admin.site.urls),


    path("api/accounts/", include("accounts.urls")),

    path("api/bracelets/", include("bracelets.urls")),

    path("api/beads/", include("beads.urls")),

    path("api/colors/", include("colors.urls")),

    path("api/disks/", include("disks.urls")),

    path("api/cart/", include("cart.urls")),

    path("api/orders/", include("orders.urls")),

    path("api/payments/", include("payments.urls")),

    path("api/shipping/", include("shipping.urls")),


    path("api/nfc/", include("nfc.urls")),

    path("api/social-links/", include("social_links.urls")),


    # Swagger
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui"
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )