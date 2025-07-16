from rest_framework.permissions import BasePermission

class CanViewOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_permission('view_commande')

class CanCreateOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_permission('create_commande')

class CanUpdateOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_permission('update_commande')

class CanDeleteOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_permission('delete_commande')





# class OrderPermission(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         return request.user.has_permission('view_commande')