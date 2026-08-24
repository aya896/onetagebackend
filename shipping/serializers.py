from rest_framework import serializers

from .models import Shipping


class ShippingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipping
        fields = "__all__"

        read_only_fields = [
            "id",
            "shipping_status",
            "shipped_at",
            "delivered_at",
        ]

    def validate_order(self, order):
        request = self.context["request"]

        if order.user != request.user:
            raise serializers.ValidationError(
                "You can only create shipping for your own order."
            )

        if order.status != "CONFIRMED":
            raise serializers.ValidationError(
                "Shipping can only be created for a confirmed order."
            )

        return order