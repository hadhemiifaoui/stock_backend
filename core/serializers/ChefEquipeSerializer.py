from rest_framework import  serializers
from ..models.chefequipe import ChefEquipe

class ChefEquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefEquipe
        fields = "__all__"