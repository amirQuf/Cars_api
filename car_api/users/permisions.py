from rest_framework.permissions import BasePermission

from .models import User

class IsSale(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            
            return False
        return request.user.role == User.SALE
    
class IsSupport(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            
            return False
        return request.user.role == User.SUPPORT