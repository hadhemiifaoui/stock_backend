

from rest_framework import serializers
from ..models.preventive import Preventive
from ..models.maintenance import MaintenanceArticle
from ..models.user import User
from .userSerializer import UserSerializer
from .MaintenanceSerializer import MaintenanceSerializer

class PreventiveSerializer(MaintenanceSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, required=False)

    class Meta(MaintenanceSerializer.Meta):
        model = Preventive
        fields = MaintenanceSerializer.Meta.fields + [
            'id',
            'user',
            'user_id',
            #'datePlanifie',
            'frequency',
            #'next_due_date',
            'startDate',
            'endDate',
            'created_at',
            'updated_at',
            'type_outillage',
            'atelier',
            'numero_outillage',
            'ref',
           # 'gamme_operatoire_main',
        ]

    def append_suffix_to_numero_outillage(self, numero_outillage, type_outillage):
        type_suffix_map = {
            'Frame': 'F',
            'Moule': 'M',
            'Tulip': 'T',
            'Jaws': 'J',
            'Head': 'H'
        }
        suffix = type_suffix_map.get(type_outillage)
        if numero_outillage and suffix and not numero_outillage.endswith(suffix):
            return f"{numero_outillage}{suffix}"
        return numero_outillage

    def create(self, validated_data):
        articles_data = validated_data.pop('articles_with_quantity', [])
        user = validated_data.pop('user_id', None)

        numero_outillage = validated_data.get('numero_outillage')
        type_outillage = validated_data.get('type_outillage')
        validated_data['numero_outillage'] = self.append_suffix_to_numero_outillage(numero_outillage, type_outillage)

        instance = Preventive.objects.create(user=user, **validated_data)
        self.handle_articles_with_quantity(instance, articles_data)
        return instance

    def update(self, instance, validated_data):
        articles_data = validated_data.pop('articles_with_quantity', [])
        user = validated_data.pop('user_id', None)

        numero_outillage = validated_data.get('numero_outillage', instance.numero_outillage)
        type_outillage = validated_data.get('type_outillage', instance.type_outillage)
        validated_data['numero_outillage'] = self.append_suffix_to_numero_outillage(numero_outillage, type_outillage)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if user:
            instance.user = user
        instance.save()

        if articles_data:
            MaintenanceArticle.objects.filter(maintenance=instance).delete()
            self.handle_articles_with_quantity(instance, articles_data)

        return instance
