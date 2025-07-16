from rest_framework import viewsets
from core.models.carteAcceptation.AcceptCarte import AcceptCarte
from core.serializers.carteAccepSerializers.acceptCarteSerializer import AcceptCarteSerializer
from rest_framework.permissions import IsAuthenticated
class AcceptCarteViewSet(viewsets.ModelViewSet):
    queryset = AcceptCarte.objects.all()
    serializer_class = AcceptCarteSerializer
    permission_classes = [IsAuthenticated]