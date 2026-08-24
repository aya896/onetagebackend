from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Bracelet, OwnedBracelet
from .serializers import (
    BraceletSerializer,
    OwnedBraceletSerializer,
)


class BraceletListView(generics.ListAPIView):
    queryset = Bracelet.objects.all()
    serializer_class = BraceletSerializer
    permission_classes = [AllowAny]


class OwnedBraceletCreateView(generics.CreateAPIView):
    serializer_class = OwnedBraceletSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OwnedBraceletListView(generics.ListAPIView):
    serializer_class = OwnedBraceletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OwnedBracelet.objects.filter(
            user=self.request.user
        )