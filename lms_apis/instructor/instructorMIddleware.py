from rest_framework.permissions import BasePermission, IsAuthenticated

class IsInstructor(BasePermission):
    
    def has_permission(self, request, view):
    
        if not request.user or not request.user.is_authenticated:
            return False
        try:
            return request.user.instructor.role == 'instructor'
        except:
            return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.instructor.user == request.user
