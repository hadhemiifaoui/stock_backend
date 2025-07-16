from rest_framework import viewsets
from ..models.supplier import Supplier
from ..serializers.supplierSerializer import SupplierSerializer
from rest_framework.permissions import IsAuthenticated

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]



#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from .serializer import SupplierSerializer
#from .models import Fournisseur


#@api_view(['GET', 'POST'])
#def list_fournisseur(request):
#    if request.method == 'GET':
#        fournisseurs = Fournisseur.objects.all()
#        serializer = SupplierSerializer(fournisseurs, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)

#    elif request.method == 'POST':
#        if isinstance(request.data, list):
#            serializer = SupplierSerializer(data=request.data, many=True)
#        else:
#            serializer = SupplierSerializer(data=request.data)

#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET', 'PUT', 'DELETE'])
#def details_fournisseur(request, id):
#    try:
#        fournisseur = Fournisseur.objects.get(id=id)
#    except Fournisseur.DoesNotExist:
#        return Response({'message': 'cet fournisseur n`existe pas'}, status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        serializer = SupplierSerializer(fournisseur)
#        return Response(serializer.data, status=status.HTTP_200_OK)

#    elif request.method == 'PUT':
#        serializer = SupplierSerializer(fournisseur, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        fournisseur.delete()
#        return Response({'message': 'Fournisseur supprimé avec succè'}, status=status.HTTP_204_NO_CONTENT)
