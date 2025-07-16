from rest_framework import serializers
from ..models.outillageHistorique import OutillageHistory

class OutillageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OutillageHistory
        fields = '__all__'
