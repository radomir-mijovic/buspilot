from rest_framework.permissions import BasePermission

from auth.models import UserTypeChoices


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.user_type == UserTypeChoices.ADMIN
        )
