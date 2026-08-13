from rest_framework import viewsets
from .models import Bead
from .serializers import BeadSerializer


class BeadViewSet(viewsets.ModelViewSet):
    queryset = Bead.objects.all()
    serializer_class = BeadSerializer