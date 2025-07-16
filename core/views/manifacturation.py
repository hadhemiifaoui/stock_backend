
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..services.availibilitieServices import is_fabriqueur_available
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from ..models.manifacturation import Manifacturation
from ..serializers.manifacturationSerializer import ManifacturationSerializer

class ManifacturationViewSet(viewsets.ModelViewSet):
    queryset = Manifacturation.objects.all()
    serializer_class = ManifacturationSerializer
    permission_classes = [IsAuthenticated]

    # def perform_update(self, serializer):
    #     user = serializer.validated_data.get('user_id') or serializer.instance.user
    #     sd = serializer.validated_data.get('start_date', serializer.instance.start_date)
    #     ed = serializer.validated_data.get('end_date', serializer.instance.end_date)
    #     if not is_fabriqueur_available(user, sd, ed):
    #         raise ValidationError({"user": "Ce fabriquant n’est pas disponible pour cette période."})
    #     serializer.save()

#to be checked !!!
    # def perform_create(self, serializer):
    #     user = serializer.validated_data.get('user_id') or serializer.instance.user
    #     sd = serializer.validated_data.get('start_date', serializer.instance.start_date)
    #     ed = serializer.validated_data.get('end_date', serializer.instance.end_date)
    #     if not is_fabriqueur_available(user, sd, ed):
    #         raise ValidationError({"user": "Ce fabriquant n’est pas disponible pour cette période."})
    #     serializer.save()

    def perform_create(self, serializer):
        user = serializer.validated_data.get('user_id')
        sd = serializer.validated_data.get('start_date')
        ed = serializer.validated_data.get('end_date')

        if not user or not sd or not ed:
            raise ValidationError({"error": "Utilisateur, date de début et date de fin sont requis."})

        if not is_fabriqueur_available(user, sd, ed):
            raise ValidationError({"user": "Ce fabriquant n’est pas disponible pour cette période."})

        serializer.save()
