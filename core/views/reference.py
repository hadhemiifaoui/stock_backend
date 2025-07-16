#
# from ..serializers.ReferenceSerializer import ReferenceSerializer
# from rest_framework import viewsets
# from ..models.References import Reference
# from rest_framework.permissions import IsAuthenticated
#
# class ReferenceViewSet(viewsets.ModelViewSet):
#     queryset = Reference.objects.all()
#     serializer_class = ReferenceSerializer
#
#     permission_classes = [IsAuthenticated]



from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.References import Reference
from ..serializers.ReferenceSerializer import ReferenceSerializer

class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
