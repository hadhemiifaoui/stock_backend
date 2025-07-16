from rest_framework import serializers
from ..models.order import Order
from ..models.supplier import Supplier
from ..models.article import Article
from ..serializers.supplierSerializer import SupplierSerializer
from ..serializers.articleSerializer import ArticleSerializer

class OrderSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), write_only=True , required=False,
        allow_null=True,
        default=None  )
    article_id = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), write_only=True  , required=False,
        allow_null=True,
        default=None  )

    class Meta:
        fields = '__all__'
        model = Order

    def create(self, validated_data):
        supplier = validated_data.pop('supplier_id', None)
        article = validated_data.pop('article_id', None)
        order = Order.objects.create(supplier=supplier,article=article, **validated_data)
        return order

    def update(self, instance, validated_data):
        if 'supplier_id' in validated_data:
            instance.supplier = validated_data.pop('supplier_id')
        if 'article_id' in validated_data:
            instance.article = validated_data.pop('article_id')
        return super().update(instance, validated_data)
