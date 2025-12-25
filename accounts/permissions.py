from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def get_obj_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        owner = getattr(obj, 'owner', None) or getattr(obj, 'buyer', None)

        if owner is None:
            return False
        
        return owner == request.user