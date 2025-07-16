
from django.urls import path
from ..views.ml_predict import PredictFmpAPIView

urlpatterns = [
    path('predict/', PredictFmpAPIView.as_view(), name='predict_fmp'),
]
