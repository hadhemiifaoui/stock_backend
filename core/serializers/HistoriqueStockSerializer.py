from rest_framework import serializers
from ..models.HistoriqueStock import HistoriqueStock

class HistoriqueStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueStock
        fields = '__all__'
