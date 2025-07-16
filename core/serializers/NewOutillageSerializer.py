from rest_framework import serializers
from ..models.newoutillage import NVoutillage
from ..models.outillageHistorique import OutillageHistory

class NewOutillageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = NVoutillage
        fields = ['id','reference','type_outillage','date_dentre','projet', 'numero_outillage','conformite', 'projet', 'validite_finale',
                  'notes' ,'created_at' , 'updated_at']

    def append_suffix_to_numero_outillage(self, numero_outillage, type_outillage):
        type_suffix_map = {
            'Frame': 'F',
            'Moule': 'M',
            'Tulip': 'T',
            'Jaws': 'J',
            'Head': 'H',
            'Pin': 'P',
            'Elargisseur':'E'
        }
        suffix = type_suffix_map.get(type_outillage)
        if numero_outillage and suffix and not numero_outillage.endswith(suffix):
            return f"{numero_outillage}{suffix}"
        return numero_outillage

    def create(self, validated_data):

        numero_outillage = validated_data.get('numero_outillage')
        type_outillage = validated_data.get('type_outillage')
        validated_data['numero_outillage'] = self.append_suffix_to_numero_outillage(numero_outillage, type_outillage)
        instance = NVoutillage.objects.create(**validated_data)
        return instance

    # def update(self, instance, validated_data):
    #     if 'type_outillage' in validated_data:
    #         instance.type_outillage = validated_data['type_outillage']
    #
    #     numero = validated_data.get('numero_outillage', instance.numero_outillage)
    #     type_ = validated_data.get('type_outillage', instance.type_outillage)
    #     instance.numero_outillage = self.append_suffix_to_numero_outillage(numero, type_)
    #
    #     for attr, value in validated_data.items():
    #         if attr not in ['numero_outillage', 'type_outillage']:
    #             setattr(instance, attr, value)
    #
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        # Save history before updating
        OutillageHistory.objects.create(
            outillage=instance,
            reference=instance.reference,
            type_outillage=instance.type_outillage,
            date_dentre=instance.date_dentre,
            numero_outillage=instance.numero_outillage,
            conformite=instance.conformite,
            projet=instance.projet,
            validite_finale=instance.validite_finale,
            notes=instance.notes
        )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Update numero_outillage with suffix
        numero = validated_data.get('numero_outillage', instance.numero_outillage)
        type_ = validated_data.get('type_outillage', instance.type_outillage)
        instance.numero_outillage = self.append_suffix_to_numero_outillage(numero, type_)

        instance.save()
        return instance
