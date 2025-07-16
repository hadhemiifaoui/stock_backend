from django.urls import path
from ..views.ml_predict1 import PredictScoreFmpView

urlpatterns = [
    path('predict1/', PredictScoreFmpView.as_view(), name='predict_score_fmp'),
]
