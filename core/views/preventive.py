from rest_framework import viewsets
from ..models.preventive import Preventive
from ..serializers.preventiveSerializer import PreventiveSerializer
from rest_framework.permissions import IsAuthenticated

class PreventiveViewSet(viewsets.ModelViewSet):
    queryset = Preventive.objects.all()
    serializer_class = PreventiveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Preventive.objects.all()
        ref = self.request.query_params.get('ref')
        type_outillage = self.request.query_params.get('type_outillage')
        atelier = self.request.query_params.get('atelier')
        user = self.request.query_params.get('user')

        if ref:
            queryset = queryset.filter(ref=ref)
        if type_outillage:
            queryset = queryset.filter(type_outillage=type_outillage)
        if atelier:
            queryset = queryset.filter(atelier=atelier)
        if user:
            queryset = queryset.filter(user=user)

        return queryset

