from django.urls import path
from ..views.ml_predict2 import PredictScore

urlpatterns = [
    path('predict2/', PredictScore.as_view(), name='predict_score'),
]
