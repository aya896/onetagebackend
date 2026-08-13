from rest_framework import serializers
from .models import Bracelet, OwnedBracelet

class BraceletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bracelet
        fields = "__all__"

class OwnedBraceletSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnedBracelet
        fields = "__all__"