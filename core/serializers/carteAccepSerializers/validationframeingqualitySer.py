from rest_framework import serializers

from core.models.carteAcceptation.validationframeingquality import ValidationFrameIngQuality

class ValidationFrameIngQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationFrameIngQuality
        fields = '__all__'