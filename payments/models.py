from django.db import models
from orders.models import Order


class Payment(models.Model):

    PAYMENT_METHODS = [
        ("COD", "Cash On Delivery"),
        ("ONLINE", "Online Payment"),
    ]

    ONLINE_PROVIDERS = [
        ("PAYPAL", "PayPal"),
        ("CARD", "Credit Card"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("FAILED", "Failed"),
        ("REFUNDED", "Refunded"),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    online_provider = models.CharField(
        max_length=20,
        choices=ONLINE_PROVIDERS,
        blank=True,
        null=True
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id}"