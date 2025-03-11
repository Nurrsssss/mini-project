from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()

class IsTrader(BasePermission):
   
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_trader()

class IsSalesRepresentative(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_sales()

class IsCustomer(BasePermission):
   
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_customer()