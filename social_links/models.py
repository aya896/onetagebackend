from django.db import models
from nfc.models import NFCProfile


class SocialLink(models.Model):

    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("linkedin", "LinkedIn"),
        ("tiktok", "TikTok"),
        ("whatsapp", "WhatsApp"),
        ("youtube", "YouTube"),
        ("x", "X"),
        ("website", "Website"),
    ]

    profile = models.ForeignKey(
        NFCProfile,
        on_delete=models.CASCADE,
        related_name="social_links"
    )

    platform = models.CharField(
        max_length=30,
        choices=PLATFORM_CHOICES
    )

    url = models.URLField()

    class Meta:
        unique_together = ("profile", "platform")

    def __str__(self):
        return f"{self.profile.full_name} - {self.platform}"