from rest_framework import serializers

from core.models.carteAcceptation.validationframeserviceouti import ValidationFrameServiceOutillage

class ValidationFrameServiceOutillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationFrameServiceOutillage
        fields = '__all__'