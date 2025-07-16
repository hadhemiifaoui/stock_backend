from rest_framework import viewsets
from ..models.curative import Curative
from ..serializers.curativeSerializer import CurativeSerializer
from rest_framework.permissions import IsAuthenticated

class CurativeViewSet(viewsets.ModelViewSet):
    queryset = Curative.objects.all()
    serializer_class = CurativeSerializer
    permission_classes = [IsAuthenticated]
