# from ..models.curative import Curative
# from ..models.maintenance import Article, MaintenanceArticle
# from .MaintenanceSerializer import MaintenanceSerializer
# from ..models.user import User
# from ..serializers.ChefEquipeSerializer import ChefEquipeSerializer
# from ..models.chefequipe import ChefEquipe
# from .userSerializer import UserSerializer
# from rest_framework import serializers
#
# class CurativeSerializer(MaintenanceSerializer):
#     user = UserSerializer(read_only=True)
#     user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True ,
#                                                  required=False, allow_null=True)
#     # demandeur = ChefEquipeSerializer(read_only=True, allow_null=True)
#     # demandeur_id = serializers.PrimaryKeyRelatedField(queryset=ChefEquipe.objects.all(), write_only=True,
#     #                                              required=False, allow_null=True)
#
#     demandeur = UserSerializer(read_only=True, allow_null=True)
#     demandeur_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True ,
#                                                  required=False, allow_null=True)
#
#     articles_with_quantity = serializers.ListField(
#         child=serializers.DictField(
#             child=serializers.IntegerField()
#         ),
#         write_only=True,
#         required=False, allow_null=True
#     )
#     class Meta(MaintenanceSerializer.Meta):
#         model = Curative
#         fields = MaintenanceSerializer.Meta.fields + [
#             'id',
#             'user',
#             'user_id',
#             'date_propose_par_demandeur',
#             'heure_propose_par_demandeur',
#             'date_propose_par_mecancien',
#             'heure_propose_par_mecancien',
#             'demandeur',
#             'demandeur_id',
#             'type_intervention',
#             'description',
#             'type_outillage',
#             'atelier',
#             'numero_outillage',
#             'articles_with_quantity',
#             'ref',
#             'type_problem',
#             'created_at',
#             'updated_at',
#         ]
#
#     def append_suffix_to_numero_outillage(self, numero_outillage, type_outillage):
#         type_suffix_map = {
#             'Frame': 'F',
#             'Moule': 'M',
#             'Tulip': 'T',
#             'Jaws': 'J',
#             'Head': 'H'
#         }
#         suffix = type_suffix_map.get(type_outillage)
#         if numero_outillage and suffix and not numero_outillage.endswith(suffix):
#             return f"{numero_outillage}{suffix}"
#         return numero_outillage
#     def create(self, validated_data):
#         articles_data = validated_data.pop('articles_with_quantity', [])
#         demandeur = validated_data.pop('demandeur_id', None)
#         user = validated_data.pop('user_id', None)
#         if user is None:
#             user = None
#         numero_outillage = validated_data.get('numero_outillage')
#         type_outillage = validated_data.get('type_outillage')
#         validated_data['numero_outillage'] = self.append_suffix_to_numero_outillage(numero_outillage, type_outillage)
#
#         instance = Curative.objects.create(user=user, demandeur=demandeur, **validated_data)
#
#         if articles_data:
#             self.handle_articles_with_quantity(instance, articles_data)
#
#         return instance
#
#     def update(self, instance, validated_data):
#         articles_data = validated_data.pop('articles_with_quantity', [])
#         user = validated_data.pop('user_id', None)
#         demandeur = validated_data.pop('demandeur_id', None)
#         if demandeur is not None:
#             instance.demandeur = demandeur
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#
#         if user is not None:
#             instance.user = user
#         numero_outillage = validated_data.get('numero_outillage', instance.numero_outillage)
#         type_outillage = validated_data.get('type_outillage', instance.type_outillage)
#         validated_data['numero_outillage'] = self.append_suffix_to_numero_outillage(numero_outillage, type_outillage)
#
#         instance.save()
#
#         if articles_data:
#             MaintenanceArticle.objects.filter(maintenance=instance).delete()
#             self.handle_articles_with_quantity(instance, articles_data)
#
#         return instance


from ..models.curative import Curative
from ..models.maintenance import Article, MaintenanceArticle
from .MaintenanceSerializer import MaintenanceSerializer
from ..models.user import User
from .userSerializer import UserSerializer
from rest_framework import serializers

class CurativeSerializer(MaintenanceSerializer):
    # Utilisateur ayant créé ou manipulé la curative (associé au FK 'user')
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True,
        required=False, allow_null=True
    )

    # Demandeur initial
    demandeur = UserSerializer(read_only=True, allow_null=True)
    demandeur_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True,
        required=False, allow_null=True
    )

    # ====== Nouveau champ outilleur ======
    outilleur = UserSerializer(read_only=True, allow_null=True)
    outilleur_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True,
        required=False, allow_null=True
    )

    articles_with_quantity = serializers.ListField(
        child=serializers.DictField(child=serializers.IntegerField()),
        write_only=True,
        required=False, allow_null=True
    )

    class Meta(MaintenanceSerializer.Meta):
        model = Curative
        fields = MaintenanceSerializer.Meta.fields + [
            'id',
            'user', 'user_id',
            'date_propose_par_demandeur',
            'heure_propose_par_demandeur',
            'date_propose_par_mecancien',
            'heure_propose_par_mecancien',
            'demandeur', 'demandeur_id',
            'outilleur', 'outilleur_id',
            'type_intervention',
            'description',
            'type_outillage',
            'atelier',
            'numero_outillage',
            'articles_with_quantity',
            'ref',
            'type_problem',
            'created_at',
            'updated_at',
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
        demandeur = validated_data.pop('demandeur_id', None)
        outilleur = validated_data.pop('outilleur_id', None)

        numero_outillage = validated_data.get('numero_outillage')
        type_outillage = validated_data.get('type_outillage')
        validated_data['numero_outillage'] = self.append_suffix_to_numero_outillage(numero_outillage, type_outillage)

        instance = Curative.objects.create(
            user=user,
            demandeur=demandeur,
            outilleur=outilleur,
            **validated_data
        )

        if articles_data:
            self.handle_articles_with_quantity(instance, articles_data)
        return instance

    def update(self, instance, validated_data):
        articles_data = validated_data.pop('articles_with_quantity', [])
        user = validated_data.pop('user_id', None)
        demandeur = validated_data.pop('demandeur_id', None)
        outilleur = validated_data.pop('outilleur_id', None)

        if user is not None:
            instance.user = user
        if demandeur is not None:
            instance.demandeur = demandeur
        if outilleur is not None:
            instance.outilleur = outilleur

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        numero_outillage = validated_data.get('numero_outillage', instance.numero_outillage)
        type_outillage = validated_data.get('type_outillage', instance.type_outillage)
        instance.numero_outillage = self.append_suffix_to_numero_outillage(numero_outillage, type_outillage)

        instance.save()

        if articles_data:
            MaintenanceArticle.objects.filter(maintenance=instance).delete()
            self.handle_articles_with_quantity(instance, articles_data)

        return instance
