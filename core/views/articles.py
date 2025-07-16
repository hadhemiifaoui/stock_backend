from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models.article import Article
from ..serializers.articleSerializer import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>[0-9]+)')
    def get_articles_by_category(self, request, category_id=None):
        articles = Article.objects.filter(category_id=category_id)
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='supplier/(?P<supplier_id>[0-9]+)')
    def get_articles_by_supplier(self, request, supplier_id=None):
        articles = Article.objects.filter(supplier_id=supplier_id)
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)


