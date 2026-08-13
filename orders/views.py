from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer

from bracelets.models import OwnedBracelet


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):

        old_order = self.get_object()

        order = serializer.save()

        if (
            old_order.status != "CONFIRMED"
            and order.status == "CONFIRMED"
        ):

            for item in order.items.all():

                OwnedBracelet.objects.create(
                    user=order.user,
                    bracelet=item.bracelet,
                    bead=item.bead,
                    color=item.color,
                    disk=item.disk,
                    engraving=item.engraving
                )