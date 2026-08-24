from rest_framework import serializers

from .models import NFCProfile
from social_links.models import SocialLink


class SocialLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialLink
        fields = ["platform", "url"]


class NFCProfileSerializer(serializers.ModelSerializer):

    social_links = SocialLinkSerializer(
        many=True,
        read_only=True
    )

    profile_image = serializers.ImageField(
        required=False,
        allow_null=True
    )

    class Meta:
        model = NFCProfile
        fields = "__all__"


class ActivateBraceletSerializer(serializers.Serializer):

    owned_bracelet_id = serializers.IntegerField()

    uid = serializers.CharField(
        max_length=100
    )

    full_name = serializers.CharField(
        max_length=150
    )

    profession = serializers.CharField(
        max_length=150
    )

    company = serializers.CharField(
        max_length=150
    )

    bio = serializers.CharField()

    email = serializers.EmailField(
        required=False,
        allow_blank=True
    )

    phone = serializers.CharField(
        required=False,
        allow_blank=True
    )

    address = serializers.CharField(
        required=False,
        allow_blank=True
    )

    profile_image = serializers.ImageField(
        required=False,
        allow_null=True
    )