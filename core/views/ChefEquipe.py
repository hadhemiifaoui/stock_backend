from ..serializers.ChefEquipeSerializer import ChefEquipeSerializer
from rest_framework import viewsets
from ..models.chefequipe import ChefEquipe
from rest_framework.permissions import IsAuthenticated

class ChefEquipeViewSet(viewsets.ModelViewSet):
    queryset = ChefEquipe.objects.all()
    serializer_class = ChefEquipeSerializer

    permission_classes = [IsAuthenticated]