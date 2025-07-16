
from rest_framework import viewsets
from core.models.carteAcceptation.validationframechefoutillage import ValidationFrameChefOutillage
from core.serializers.carteAccepSerializers.validationframechefoutiSer import ValidationFrameChefOutillageSerializer
from rest_framework.permissions import IsAuthenticated
class ValidationFrameChefOutillageViewSet(viewsets.ModelViewSet):
    queryset = ValidationFrameChefOutillage.objects.all()
    serializer_class = ValidationFrameChefOutillageSerializer

    permission_classes = [IsAuthenticated]