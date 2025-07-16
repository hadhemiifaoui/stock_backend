
from rest_framework import serializers
from core.models.carteAcceptation.AcceptCarte import AcceptCarte
from core.serializers.manifacturationSerializer import ManifacturationSerializer
from core.models.manifacturation import Manifacturation

from core.serializers.carteAccepSerializers.validationframechefoutiSer import ValidationFrameChefOutillageSerializer
from core.serializers.carteAccepSerializers.validationframeserviceOutillageSer import ValidationFrameServiceOutillageSerializer
from core.serializers.carteAccepSerializers.validationframeingqualitySer import ValidationFrameIngQualitySerializer
from core.serializers.carteAccepSerializers.validationoutillageingQualSer import ValidationOutillageIgenQualitySerializer
from core.serializers.carteAccepSerializers.validationoutillageServiceOutillageSer import ValidationOutillageServiceOutillageSerializer

from core.models.carteAcceptation.validationframechefoutillage import ValidationFrameChefOutillage
from core.models.carteAcceptation.validationframeserviceouti import ValidationFrameServiceOutillage
from core.models.carteAcceptation.validationframeingquality import ValidationFrameIngQuality
from core.models.carteAcceptation.validationoutillageservouti import ValidationOutillageServiceOutillage
from core.models.carteAcceptation.validationoutillageingquality import ValidationOutillageIgenQuality


class AcceptCarteSerializer(serializers.ModelSerializer):
    manifacturation = ManifacturationSerializer(read_only=True)

    manifacturation_id = serializers.PrimaryKeyRelatedField(
        queryset=Manifacturation.objects.all(),
        write_only=True
    )

    #order = OrderCarteAcceptationSerializer(required=False)
    validationframechefoutillage = ValidationFrameChefOutillageSerializer(required=False)
    validationframeso = ValidationFrameServiceOutillageSerializer(required=False)
    validationframeingquality = ValidationFrameIngQualitySerializer(required=False)
    validationoutillageso = ValidationOutillageServiceOutillageSerializer(required=False)
    validationoutillageingquality = ValidationOutillageIgenQualitySerializer(required=False)

    class Meta:
        model = AcceptCarte
        fields = [
            'id',
            'manifacturation',
            'nom','titre','type_outillage','numero_outillage','ref','indice', 'rmq' , 'date_ordre',
            'manifacturation_id',
            #'order',
            'validationframechefoutillage',
            'validationframeso',
            'validationframeingquality',
            'validationoutillageso',
            'validationoutillageingquality',
            'updated_at'
        ]

    def create(self, validated_data):
        # Extract nested parts
       # order_data = validated_data.pop('order', None)
        chef_data = validated_data.pop('validationFchefO', None)
        serv_data = validated_data.pop('validationFservO', None)
        ing_data = validated_data.pop('validationFingQual', None)
        out_serv_data = validated_data.pop('validationOutServOut', None)
        out_ing_data = validated_data.pop('validationOutIngQual', None)

        # Create main AcceptCarte
        manifacturation = validated_data.pop('manifacturation_id')
        accept_carte = AcceptCarte.objects.create(manifacturation=manifacturation, **validated_data)

        # Create each nested part with carte=accept_carte
        # if order_data:
        #     OrderCarteAcceptation.objects.create(carte=accept_carte, **order_data)
        if chef_data:
            ValidationFrameChefOutillage.objects.create(carte=accept_carte, **chef_data)
        if serv_data:
            ValidationFrameServiceOutillage.objects.create(carte=accept_carte, **serv_data)
        if ing_data:
            ValidationFrameIngQuality.objects.create(carte=accept_carte, **ing_data)
        if out_serv_data:
            ValidationOutillageServiceOutillage.objects.create(carte=accept_carte, **out_serv_data)
        if out_ing_data:
            ValidationOutillageIgenQuality.objects.create(carte=accept_carte, **out_ing_data)

        return accept_carte

    def update(self, instance, validated_data):
        # Update manifacturation if needed
        if 'manifacturation_id' in validated_data:
            instance.manifacturation = validated_data.pop('manifacturation_id')

        # Nested update helper
        def update_nested(model_class, related_name, data):
            try:
                obj = model_class.objects.get(carte=instance)
                for attr, val in data.items():
                    setattr(obj, attr, val)
                obj.save()
            except model_class.DoesNotExist:
                model_class.objects.create(carte=instance, **data)


        # if 'order' in validated_data:
        #     update_nested(OrderCarteAcceptation, 'order', validated_data.pop('order'))
        if 'validationFchefO' in validated_data:
            update_nested(ValidationFrameChefOutillage, 'validationFchefO', validated_data.pop('validationFchefO'))
        if 'validationFservO' in validated_data:
            update_nested(ValidationFrameServiceOutillage, 'validationFservO', validated_data.pop('validationFservO'))
        if 'validationFingQual' in validated_data:
            update_nested(ValidationFrameIngQuality, 'validationFingQual', validated_data.pop('validationFingQual'))
        if 'validationOutServOut' in validated_data:
            update_nested(ValidationOutillageServiceOutillage, 'validationOutServOut', validated_data.pop('validationOutServOut'))
        if 'validationOutIngQual' in validated_data:
            update_nested(ValidationOutillageIgenQuality, 'validationOutIngQual', validated_data.pop('validationOutIngQual'))

        instance.save()
        return instance
