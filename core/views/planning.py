from rest_framework import viewsets
from ..models.planning import Planning
from ..serializers.planningSerializer import PlanningSerializer
from rest_framework.permissions import IsAuthenticated

class PlanningViewSet(viewsets.ModelViewSet):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer
    permission_classes = [IsAuthenticated]