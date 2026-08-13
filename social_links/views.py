from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import SocialLink
from .serializers import SocialLinkSerializer

from nfc.models import NFCProfile



class SocialLinkListCreateView(generics.ListCreateAPIView):

    serializer_class = SocialLinkSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):

        return SocialLink.objects.filter(
            profile__bracelet__user=self.request.user
        )


    def perform_create(self, serializer):

        profile_id = self.request.data.get("profile")


        profile = NFCProfile.objects.get(
            id=profile_id,
            bracelet__user=self.request.user
        )


        serializer.save(
            profile=profile
        )





class SocialLinkDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SocialLinkSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):

        return SocialLink.objects.filter(
            profile__bracelet__user=self.request.user
        )