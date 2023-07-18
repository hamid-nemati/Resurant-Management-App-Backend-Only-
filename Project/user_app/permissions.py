from rest_framework import permissions
from .models import RestaurantUser

class IsOwnerOfThisProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user = RestaurantUser.objects.get(username=request.query_params['username'])
        except:
            return False

        if request.user.is_superuser or request.user.username == user.username:
            return True
        else:
            return False