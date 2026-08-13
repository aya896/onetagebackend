from rest_framework import viewsets
from .models import Disk
from .serializers import DiskSerializer


class DiskViewSet(viewsets.ModelViewSet):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer