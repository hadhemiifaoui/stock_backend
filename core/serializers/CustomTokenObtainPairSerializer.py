from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'user_name'

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user_name': self.user.user_name})
        return data
