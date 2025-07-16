from rest_framework import serializers
from ..models.stock import Stock
from ..models.article import Article
from ..models.HistoriqueStock import HistoriqueStock
class StockSerializer(serializers.ModelSerializer):
    article_id = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), write_only=True)
    article = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        article = validated_data.pop('article_id')
        stock = Stock.objects.create(article=article, **validated_data)
        return stock

    def update(self, instance, validated_data):
        HistoriqueStock.objects.create(
            stock=instance,
            quantity = instance.quantity,
            received_commands = instance.received_commands,
        total_quantity_used = instance.total_quantity_used,
        consomation_annuelle = instance.consomation_annuelle,
        location =  instance.location,
        reorder_level = instance.reorder_level,
        delai_approvisionnement = instance.delai_approvisionnement,
        seuil_min = instance.seuil_min,
        virtual_stock = instance.virtual_stock,
        ecart_stock = instance.ecart_stock,
        a_commande = instance.a_commande,
            article= instance.article
        )
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if 'article_id' in validated_data:
            instance.article = validated_data.pop('article_id')
        return super().update(instance, validated_data)

    def get_article(self, obj):
        article_data = {
            "id": obj.article.id,
            "name": obj.article.name,
            "description": obj.article.description,
            "category": {
                "id": obj.article.category.id,
                "name": obj.article.category.nom
            },
            "unity": obj.article.unity,
            "image": obj.article.image.url if obj.article.image else None,
            "supplier": {
                "id": obj.article.supplier.id,
                "name": obj.article.supplier.nom
            }
        }
        return article_data if obj.article else None
