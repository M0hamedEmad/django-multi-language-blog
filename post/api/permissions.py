from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        """
            Allows access only if post owner same user that login .
        """
        return request.method in SAFE_METHODS or obj.author == request.user

class IsOwnerOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        """
            Allows access only if post owner same user that login .
        """
        return request.method in SAFE_METHODS or obj.user == request.user        