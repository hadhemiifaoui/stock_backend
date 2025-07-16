
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.ml_predict.predict import predict_fmp
from rest_framework.permissions import IsAuthenticated

class PredictFmpAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        input_data = request.data
        if not input_data:
            return Response({'error': 'No input data provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            prediction = predict_fmp(input_data)
            return Response({'prediction': prediction})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
