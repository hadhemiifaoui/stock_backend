from rest_framework import viewsets
from core.models.carteAcceptation.validationoutillageservouti import ValidationOutillageServiceOutillage
from core.serializers.carteAccepSerializers.validationoutillageServiceOutillageSer import ValidationOutillageServiceOutillageSerializer
from rest_framework.permissions import IsAuthenticated
class ValidationOutillageServiceOutillageViewSet(viewsets.ModelViewSet):
    queryset = ValidationOutillageServiceOutillage.objects.all()
    serializer_class = ValidationOutillageServiceOutillageSerializer

    permission_classes = [IsAuthenticated]