from rest_framework import serializers
from ..models import User
from ..models.role import Role
from ..serializers.roleSerializer import RoleSerializer

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), write_only=True)
    password = serializers.CharField(write_only=True, required=False)
    password_success = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            "role": {"required": False},
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        role = validated_data.pop('role_id', None)
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        if role:
            user.role = role

        user.save()
        return user

    def validate(self, attrs):
        if self.instance is None and not attrs.get('password'):
            raise serializers.ValidationError({ "Le champs mot de passe est obligatoire."})
        return attrs

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        role = validated_data.pop('role_id', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        if role:
            instance.role = role

        instance.save()
        return instance

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Le mot de pass doit etre minimum 8 charactères")
        return value

    def get_password_success(self, obj):

        return True

