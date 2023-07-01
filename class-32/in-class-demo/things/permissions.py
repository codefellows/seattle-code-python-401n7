from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if my method returns True, then the request is authorized
        # else 403 forbidden

        # hover over SAFE_METHODS to see the list
        if request.method in permissions.SAFE_METHODS:
            return True

        # else, check if the requesting user, is the same as the object's owner
        return obj.owner == request.user
