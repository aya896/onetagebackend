from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Bracelet
from .models import Bracelet, OwnedBracelet
from .serializers import (
    BraceletSerializer,
    OwnedBraceletSerializer,
)


class BraceletListCreateView(generics.ListCreateAPIView):
    queryset = Bracelet.objects.all()
    serializer_class = BraceletSerializer

class OwnedBraceletListCreateView(generics.ListCreateAPIView):
    queryset = OwnedBracelet.objects.all()
    serializer_class = OwnedBraceletSerializer

class OwnedBraceletListView(generics.ListAPIView):

    serializer_class = OwnedBraceletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OwnedBracelet.objects.filter(
            user=self.request.user
        )