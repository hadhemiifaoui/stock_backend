from rest_framework import  serializers

from ..models.repport import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        field = '__all__'
