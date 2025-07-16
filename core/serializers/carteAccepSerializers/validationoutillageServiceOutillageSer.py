from rest_framework import serializers

from core.models.carteAcceptation.validationoutillageservouti import ValidationOutillageServiceOutillage

class ValidationOutillageServiceOutillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationOutillageServiceOutillage
        fields = '__all__'