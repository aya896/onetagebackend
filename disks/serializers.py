from rest_framework import serializers
from .models import Disk


class DiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disk
        fields = "__all__"