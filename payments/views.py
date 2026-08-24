from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(
            order__user=self.request.user
        )

    def perform_create(self, serializer):

        order = serializer.validated_data["order"]

        payment = serializer.save(
            amount=order.total_price
        )

        # For MVP:
        # COD is considered paid/confirmed immediately.
        if payment.payment_method == "COD":

            payment.status = "PAID"
            payment.save()

            order.status = "CONFIRMED"
            order.save()