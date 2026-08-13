from django.db import models
from django.conf import settings

from bracelets.models import Bracelet
from beads.models import Bead
from colors.models import Color
from disks.models import Disk


class CartItem(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )

    bracelet = models.ForeignKey(
        Bracelet,
        on_delete=models.CASCADE
    )

    bead = models.ForeignKey(
        Bead,
        on_delete=models.CASCADE
    )

    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE
    )

    disk = models.ForeignKey(
        Disk,
        on_delete=models.CASCADE
    )

    engraving = models.CharField(
        max_length=100,
        blank=True
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.bracelet.name}"