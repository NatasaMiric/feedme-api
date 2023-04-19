from rest_framework import permissions

# Code is taken from Code Institute walkthrough project
# https://github.com/Code-Institute-Solutions/drf-api/blob/025406b0a0fb365a1931747b596c33fd3ba2a6dc/drf_api/permissions.py


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
