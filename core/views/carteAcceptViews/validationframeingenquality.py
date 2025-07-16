from rest_framework import viewsets
from core.models.carteAcceptation.validationframeingquality import ValidationFrameIngQuality
from core.serializers.carteAccepSerializers.validationframeingqualitySer import ValidationFrameIngQualitySerializer
from rest_framework.permissions import IsAuthenticated
class ValidationFrameIngQualityViewSet(viewsets.ModelViewSet):
    queryset = ValidationFrameIngQuality.objects.all()
    serializer_class = ValidationFrameIngQualitySerializer

    permission_classes = [IsAuthenticated]