from ..models.maintenance import Maintenance, MaintenanceArticle
from ..models.article import Article
from rest_framework import serializers
from .MaintenanceArticleSerializer import MaintenanceArticleSerializer
from ..models.stock import Stock
class MaintenanceSerializer(serializers.ModelSerializer):

    articles_with_quantity = serializers.ListField(
        child=serializers.DictField( child=serializers.CharField() ), write_only=True , required=False
    )
    article_details = serializers.SerializerMethodField()

    class Meta:
        model = Maintenance
        fields = [ 'id','maint_type', 'statut', 'user', 'articles_with_quantity', 'article_details']

    def get_article_details(self, obj):
        return MaintenanceArticleSerializer(MaintenanceArticle.objects.filter(maintenance=obj), many=True).data


    def handle_articles_with_quantity(self, instance, articles_data):
        for item in articles_data:
            article = Article.objects.get(id=item['article'])
            #quantity_used = item['quantity_consume']
            quantity_used = int(item['quantity_consume'])

            MaintenanceArticle.objects.create(
                maintenance=instance,
                article=article,
                quantite_consume=quantity_used
            )

            try:
                # stock = Stock.objects.get(article=article)
                # stock.total_quantity_used += quantity_used
                # stock.quantity = max(stock.quantity - quantity_used, 0)
                # stock.save()
                stock = Stock.objects.get(article=article)
                stock.total_quantity_used += quantity_used
                stock.virtual_stock = max(stock.virtual_stock - quantity_used, 0)
                stock.save()

            except Stock.DoesNotExist:
                print(f" stock not found for article {article.id}")