from rest_framework import serializers

from .articleSerializer import ArticleSerializer
from ..models.manifacturation import ManifacturationArticle


class ManifacturationArticleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model= ManifacturationArticle
        fields = ["article" , "quantite_consume"]