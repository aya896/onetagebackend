from django.db import models

from bracelets.models import OwnedBracelet


class NFCProfile(models.Model):

    bracelet = models.OneToOneField(
        OwnedBracelet,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    full_name = models.CharField(max_length=150)

    profession = models.CharField(max_length=150)

    company = models.CharField(max_length=150)

    bio = models.TextField()

    email = models.EmailField(blank=True)

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    address = models.CharField(
        max_length=255,
        blank=True
    )

    profile_image = models.ImageField(
    upload_to="profiles/",
    null=True,
    blank=True
)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name