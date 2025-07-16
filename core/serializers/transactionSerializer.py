
from rest_framework import serializers
from ..models.transaction import Transaction
from ..models.user import User
from ..models.stock import Stock
from  ..serializers.stockSerializer import StockSerializer
from ..serializers.userSerializer import UserSerializer


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stock = StockSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    stock_id = serializers.PrimaryKeyRelatedField(queryset=Stock.objects.all(), write_only=True)
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self , validated_data):
       user = validated_data.pop('user_id')
       stock = validated_data.pop('stock_id')
       transaction = Transaction.objects.create(user=user , stock=stock , **validated_data)
       return transaction


    def update(self, instance, validated_data):
        if 'user_id' in validated_data:
            instance.user = validated_data.pop('user_id')
        if 'stock_id' in validated_data:
            instance.stock = validated_data.pop('stock_id')
        return super().update(instance , validated_data)