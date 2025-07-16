from django.urls import path
from ..views.socket import low_stock_alerts  # your view function or class

urlpatterns = [
    path('low-stock-alerts/', low_stock_alerts, name='low-stock-alerts'),
]
