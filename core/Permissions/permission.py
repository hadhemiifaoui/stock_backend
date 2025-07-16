from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist
class HasRolePermission(BasePermission):
    def has_permission(self, request, view):
        required_permission = getattr(view, 'required_permission', None)
        if not required_permission:
            return True

        if not request.user.is_authenticated:
            return False

        try:

            user_role = request.user.role
            if user_role and hasattr(user_role, 'permissions'):
                role_permissions = user_role.permissions
                return role_permissions.get(required_permission, False)

        except ObjectDoesNotExist:
            return False

        return False
