
from django.urls import path
from core.socket import StockAlertConsumer
from core.socket1 import PreventiveAlertConsumer
from core.socket2 import ValidationFrameAlertConsumer
from core.socket3 import CurativeAlertConsumer
websocket_urlpatterns = [
    path("ws/alerts/stock/", StockAlertConsumer.as_asgi()),
    path("ws/alerts/preventive/", PreventiveAlertConsumer.as_asgi()),
    path("ws/alerts/validationframe/", ValidationFrameAlertConsumer.as_asgi()),
    path("ws/alerts/curative/", CurativeAlertConsumer.as_asgi())
    ]