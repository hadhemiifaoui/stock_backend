from rest_framework import viewsets
from core.models.carteAcceptation.validationoutillageingquality import ValidationOutillageIgenQuality
from core.serializers.carteAccepSerializers.validationoutillageingQualSer import ValidationOutillageIgenQualitySerializer
from rest_framework.permissions import IsAuthenticated
class ValidationOutillageIgenQualityViewSet(viewsets.ModelViewSet):
    queryset = ValidationOutillageIgenQuality.objects.all()
    serializer_class = ValidationOutillageIgenQualitySerializer

    permission_classes = [IsAuthenticated]