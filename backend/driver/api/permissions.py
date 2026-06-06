from rest_framework import permissions

from auth.models import UserTypeChoices


class BaseUserDriverPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.user_type == UserTypeChoices.DRIVER
        )
