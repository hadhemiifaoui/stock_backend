from rest_framework import viewsets
from ..models.setting import Setting
from ..serializers.settingSerializers import SettingSerializer
from rest_framework.permissions import IsAuthenticated

class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = [IsAuthenticated]