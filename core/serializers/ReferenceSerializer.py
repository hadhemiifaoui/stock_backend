from rest_framework import serializers

from ..models.References import Reference

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = "__all__"



