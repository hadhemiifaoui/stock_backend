from rest_framework import serializers

from .articleSerializer import ArticleSerializer
from ..models.maintenance import MaintenanceArticle


class MaintenanceArticleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model= MaintenanceArticle
        fields = ["article" , "quantite_consume"]