from functools import wraps
from typing import Callable

from django.shortcuts import redirect


def admin_permission_required(view_func: Callable) -> Callable:
    @wraps(view_func)
    def _authenticated_view(request, *args, **kwargs):
        if not request.user.is_admin:
            return redirect("auth:login")

        return view_func(request, *args, **kwargs)

    return _authenticated_view
