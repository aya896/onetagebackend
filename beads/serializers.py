from rest_framework import serializers
from .models import Bead


class BeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bead
        fields = "__all__"