from rest_framework import viewsets
from ..models.newoutillage import NVoutillage
from ..serializers.NewOutillageSerializer import NewOutillageSerialzer
from rest_framework.permissions import IsAuthenticated

class NVoutillageViewSet(viewsets.ModelViewSet):
    queryset = NVoutillage.objects.all()
    serializer_class = NewOutillageSerialzer
    permission_classes = [IsAuthenticated]
