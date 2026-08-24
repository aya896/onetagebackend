from django.utils import timezone

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Shipping
from .serializers import ShippingSerializer


class ShippingViewSet(viewsets.ModelViewSet):

    serializer_class = ShippingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Shipping.objects.filter(
            order__user=self.request.user
        )

    def perform_update(self, serializer):

        old_status = self.get_object().shipping_status

        shipping = serializer.save()

        if (
            old_status != "SHIPPED"
            and shipping.shipping_status == "SHIPPED"
        ):
            shipping.shipped_at = timezone.now()
            shipping.save()

        if (
            old_status != "DELIVERED"
            and shipping.shipping_status == "DELIVERED"
        ):
            shipping.delivered_at = timezone.now()
            shipping.save()