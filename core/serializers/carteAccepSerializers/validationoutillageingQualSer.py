from rest_framework import serializers

from core.models.carteAcceptation.validationoutillageingquality import ValidationOutillageIgenQuality

class ValidationOutillageIgenQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationOutillageIgenQuality
        fields = '__all__'