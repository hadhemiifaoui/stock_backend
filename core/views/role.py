from rest_framework import viewsets
from ..models.role import Role
from ..serializers.roleSerializer import RoleSerializer
from rest_framework.permissions import IsAuthenticated

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]