from rest_framework import generics
from ..models.outillageHistorique import OutillageHistory
from ..serializers.outillageHistorySerializer import OutillageHistorySerializer

class OutillageHistoryListView(generics.ListAPIView):
    serializer_class = OutillageHistorySerializer

    def get_queryset(self):
        outillage_id = self.kwargs['outillage_id']
        return OutillageHistory.objects.filter(outillage_id=outillage_id).order_by('-updated_at')
