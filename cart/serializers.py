from rest_framework import serializers

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"

        read_only_fields = [
            "id",
            "user",
            "total_price",
            "created_at",
        ]

    def create(self, validated_data):
        bracelet = validated_data["bracelet"]
        quantity = validated_data.get("quantity", 1)

        validated_data["total_price"] = bracelet.price * quantity

        return super().create(validated_data)

    def update(self, instance, validated_data):
        bracelet = validated_data.get(
            "bracelet",
            instance.bracelet
        )

        quantity = validated_data.get(
            "quantity",
            instance.quantity
        )

        validated_data["total_price"] = bracelet.price * quantity

        return super().update(instance, validated_data)