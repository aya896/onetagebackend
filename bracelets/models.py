from django.db import models
from django.conf import settings

from beads.models import Bead
from colors.models import Color
from disks.models import Disk


class Bracelet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="bracelets/")

    def __str__(self):
        return self.name


class OwnedBracelet(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_bracelets"
    )

    bracelet = models.ForeignKey(
        Bracelet,
        on_delete=models.CASCADE,
        related_name="owned_bracelets"
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

    configuration = models.JSONField(
        default=dict,
        blank=True
    )

    engraving = models.CharField(
        max_length=100,
        blank=True
    )

    uid = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        db_index=True
    )

    activated = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.bracelet.name}"