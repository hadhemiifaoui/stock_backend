from rest_framework import viewsets
from ..models.order import Order
from ..serializers.orderSerializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
















# from rest_framework import viewsets
# from ..models.order import Order
# from ..serializers.orderSerializer import OrderSerializer
# from ..services.stock_services import update_stock_quantity
# from .orderPermission import CanViewOrder, CanCreateOrder, CanUpdateOrder, CanDeleteOrder
#
#
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#     def get_permissions(self):
#
#         if self.action == 'list' or self.action == 'retrieve':
#             permission_classes = [CanViewOrder]
#         elif self.action == 'create':
#             permission_classes = [CanCreateOrder]
#         elif self.action == 'update' or self.action == 'partial_update':
#             permission_classes = [CanUpdateOrder]
#         elif self.action == 'destroy':
#             permission_classes = [CanDeleteOrder]
#         else:
#             permission_classes = []
#
#         return [permission() for permission in permission_classes]
#
#     def perform_create(self, serializer):
#         order = serializer.save()
#
#         update_stock_quantity(
#             order.article.id,
#             quantity_added=order.quantity_cmd,
#             quantity_removed=0
#         )
#
#     def perform_update(self, serializer):
#         order = serializer.save()
#         update_stock_quantity(
#             order.article.id,
#             quantity_added=order.quantity_cmd,
#             quantity_removed=0
#         )
