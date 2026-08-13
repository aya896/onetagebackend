from django.db import models
from orders.models import Order


class Shipping(models.Model):

    STATUS_CHOICES = [
        ("PREPARING", "Preparing"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="shipping"
    )

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    city = models.CharField(max_length=100)

    address = models.TextField()

    postal_code = models.CharField(
        max_length=20,
        blank=True
    )

    shipping_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PREPARING"
    )

    shipped_at = models.DateTimeField(
        null=True,
        blank=True
    )

    delivered_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Shipping #{self.id}"