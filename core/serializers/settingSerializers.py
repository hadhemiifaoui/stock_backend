from ..models.user import User
from rest_framework import serializers


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'


