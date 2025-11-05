from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasicPermission):
    def get_obj_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return owner.obj == request.user