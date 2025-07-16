from rest_framework import viewsets
from ..models.test import Test
from ..serializers.TestSerializer import TestSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()  # Optional but good to include
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Check if it's a list for bulk POST
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
