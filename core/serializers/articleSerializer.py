from rest_framework import serializers
from ..models.article import Article
from ..models.supplier import Supplier
from ..models.category import Category
from ..models.stock import Stock
from ..serializers.supplierSerializer import SupplierSerializer
from ..serializers.categorySerializer import CategorySerializer

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), write_only=True)

    stock = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        category = validated_data.pop('category_id')
        supplier = validated_data.pop('supplier_id')
        article = Article.objects.create(category=category, supplier=supplier, **validated_data)
        return article

    def update(self, instance, validated_data):
        if 'category_id' in validated_data:
            instance.category = validated_data.pop('category_id')
        if 'supplier_id' in validated_data:
            instance.supplier = validated_data.pop('supplier_id')
        return super().update(instance, validated_data)

    def get_stock(self, obj):
        stock = Stock.objects.filter(article=obj).first()
        return {
            "id": stock.id,
            "quantity": stock.quantity,
            "location": stock.location,
            "reorder_level": stock.reorder_level
        } if stock else None
