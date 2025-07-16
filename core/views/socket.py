
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from ..models.carteAcceptation.validationframechefoutillage import ValidationFrameChefOutillage
from ..models.stock import Stock
from ..serializers.stockSerializer import StockSerializer
from ..models.preventive import Preventive
from ..models.curative import Curative
@api_view(['GET'])
def low_stock_alerts(request):
    low_stocks = Stock.objects.filter(quantity__lte=F('seuil_min'))
    serializer = StockSerializer(low_stocks, many=True)
    return Response(serializer.data)

FREQUENCY_TO_DAYS = {
    "1 month": 30,
    "2 months": 60,
    "3 months": 90,
    "4 months": 120,
    "6 months": 180,
}

@api_view(['GET'])
def all_preventive_alerts(request):
    today = date.today()
    print(f"Today's date: {today}")

    all_preventives = Preventive.objects.all()
    alerts = []

    for preventive in all_preventives:
        frequency_label = preventive.frequency
        frequency_days = FREQUENCY_TO_DAYS.get(frequency_label)

        if not frequency_days:
            continue

        days_diff = (today - preventive.endDate).days
        print(f"Checking preventive {preventive.id}: endDate={preventive.endDate}, days_diff={days_diff}, freq_days={frequency_days}")

        if days_diff >= 0 and days_diff >= frequency_days:
            msg = preventive.check_and_alert()
            if msg:
                alerts.append({"id": preventive.id, "message": msg})

    return Response(alerts)

@api_view(['GET'])
def validation_frame_alerts(request):
    alerts = []
    for vf in ValidationFrameChefOutillage.objects.select_related('carte').all():
        msg = vf.check_and_alert()
        if msg:
            alerts.append({
                "id": vf.id,
                "carte_id": vf.carte_id,
                "message": msg
            })
    return Response(alerts)



@api_view(['GET'])
def curative_alerts(request):
    alerts = []
    curatives = Curative.objects.filter(statut="Invalide")
    for curative in curatives:
        message = curative.check_and_alert()
        if message:
            alerts.append({"id": curative.id, "message": message})
    return Response(alerts)