from rest_framework import serializers

from core.models.carteAcceptation.validationframechefoutillage import ValidationFrameChefOutillage

class ValidationFrameChefOutillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationFrameChefOutillage
        fields = '__all__'