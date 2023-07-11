from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:     # Authenticated users only can see list view
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # Read permissions are allowed to any request so we'll always
            return True                                 # allow GET, HEAD, or OPTIONS requests
            
        return obj.author == request.user    # Write permissions are only allowed to the author of a post