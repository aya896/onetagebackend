from rest_framework import serializers

from .models import Payment
from orders.models import Order


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"

        read_only_fields = [
            "id",
            "amount",
            "transaction_id",
            "status",
            "created_at",
        ]

    def validate_order(self, order):
        request = self.context["request"]

        if order.user != request.user:
            raise serializers.ValidationError(
                "You can only pay for your own orders."
            )

        if order.status == "CANCELLED":
            raise serializers.ValidationError(
                "You cannot pay for a cancelled order."
            )

        return order

    def validate(self, attrs):
        payment_method = attrs.get("payment_method")
        online_provider = attrs.get("online_provider")

        if payment_method == "ONLINE" and not online_provider:
            raise serializers.ValidationError({
                "online_provider": "This field is required for online payment."
            })

        if payment_method == "COD":
            attrs["online_provider"] = None

        return attrs