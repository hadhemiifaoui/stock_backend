from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.maintenance import Maintenance, MaintenanceArticle
from ..serializers.MaintenanceSerializer import MaintenanceSerializer
from ..models.article import Article
from django.db import transaction
from rest_framework.permissions import IsAuthenticated

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [IsAuthenticated]
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        articles_with_quantity = data.pop('articles_with_quantity', [])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        maintenance = serializer.save()

        for item in articles_with_quantity:
            article_id = item.get('article')
            quantity_consume = item.get('quantity_consume')

            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                transaction.set_rollback(True)
                return Response({"error": f"Article ID {article_id} not found."}, status=status.HTTP_400_BAD_REQUEST)

            if article.stock.quantity < quantity_consume:
                transaction.set_rollback(True)
                return Response({"error": f"Not enough stock for article {article.name}"}, status=status.HTTP_400_BAD_REQUEST)


            MaintenanceArticle.objects.create(
                maintenance=maintenance,
                article=article,
                quantite_consume=quantity_consume
            )


            article.stock.quantity -= quantity_consume
            article.stock.save()

        return Response(self.get_serializer(maintenance).data, status=status.HTTP_201_CREATED)
