from rest_framework import status

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework.generics import RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404


from bracelets.models import OwnedBracelet
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes

from .models import NFCProfile

from .serializers import (
    NFCProfileSerializer,
    ActivateBraceletSerializer
)



class ActivateBraceletView(APIView):

    permission_classes = [IsAuthenticated]

    serializer_class = ActivateBraceletSerializer


    def post(self, request):

        # Validate incoming data
        serializer = ActivateBraceletSerializer(
            data=request.data
        )


        if not serializer.is_valid():

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


        data = serializer.validated_data


        # Find bracelet and check owner
        bracelet = get_object_or_404(
            OwnedBracelet,
            id=data["owned_bracelet_id"],
            user=request.user
        )


        # Check if already activated
        if bracelet.activated:

            return Response(
                {
                    "error": "Bracelet already activated"
                },
                status=status.HTTP_400_BAD_REQUEST
            )



        # Save NFC UID and activate bracelet

        bracelet.uid = data["uid"]

        bracelet.activated = True

        bracelet.save()



        # Create NFC Profile

        profile = NFCProfile.objects.create(

            bracelet=bracelet,

            full_name=data["full_name"],

            profession=data["profession"],

            company=data["company"],

            bio=data["bio"],

            email=data.get("email", ""),

            phone=data.get("phone", ""),

            address=data.get("address", "")
        )



        response_serializer = NFCProfileSerializer(
            profile
        )


        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )





class NFCProfileDetailView(RetrieveUpdateAPIView):

    serializer_class = NFCProfileSerializer

    permission_classes = [IsAuthenticated]

    parser_classes = [
        MultiPartParser,
        FormParser
    ]


    def get_object(self):

        bracelet = get_object_or_404(
            OwnedBracelet,
            id=self.kwargs["bracelet_id"],
            user=self.request.user
        )

        return bracelet.profile



class ScanBraceletView(APIView):

    permission_classes = [AllowAny]


    def get(self, request, uid):

        bracelet = get_object_or_404(
            OwnedBracelet,
            uid=uid,
            activated=True
        )


        serializer = NFCProfileSerializer(
            bracelet.profile
        )


        return Response(
            serializer.data
        )