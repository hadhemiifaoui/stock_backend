from rest_framework import viewsets
from ..models.repport import Report
from ..serializers.reportSerializer import ReportSerializer
from rest_framework.permissions import IsAuthenticated

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]