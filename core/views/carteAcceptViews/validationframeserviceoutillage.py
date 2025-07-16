from rest_framework import viewsets
from core.models.carteAcceptation.validationframeserviceouti import ValidationFrameServiceOutillage
from core.serializers.carteAccepSerializers.validationframeserviceOutillageSer import ValidationFrameServiceOutillageSerializer
from rest_framework.permissions import IsAuthenticated
class ValidationFrameServiceOutillageViewSet(viewsets.ModelViewSet):
    queryset = ValidationFrameServiceOutillage.objects.all()
    serializer_class = ValidationFrameServiceOutillageSerializer

    permission_classes = [IsAuthenticated]