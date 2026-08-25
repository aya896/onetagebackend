from decimal import Decimal

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer

from bracelets.models import OwnedBracelet


class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):

        order = serializer.save(
            user=self.request.user
        )

        total = Decimal("0.00")

        for item in order.items.all():
            total += item.total_price

        order.total_price = total
        order.save()
def perform_update(self, serializer):

    old_status = self.get_object().status

    order = serializer.save()

    if (
        old_status != "CONFIRMED"
        and order.status == "CONFIRMED"
    ):

        for item in order.items.all():

            OwnedBracelet.objects.create(
                user=order.user,
                bracelet=item.bracelet,
                bead=item.bead,
                color=item.color,
                disk=item.disk,
                configuration=item.configuration,
                engraving=item.engraving
            )