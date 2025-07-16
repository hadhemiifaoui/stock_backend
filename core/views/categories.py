from rest_framework import viewsets
from ..models.category import Category
from ..serializers.categorySerializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]