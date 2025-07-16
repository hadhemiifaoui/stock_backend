from rest_framework import serializers
from ..models.stock_history import StockHistory
class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = StockHistory

