from rest_framework import permissions
from .models import RestaurantUser, Restaurant, Food, Order, FavoriteList


class Is_A_Manager(permissions.BasePermission):
    """ for Creat a restaurant """

    def has_permission(self, request, view):
        try:
            restaurant_manager = RestaurantUser.objects.get(username=request.user.username)
        except:
            return False

        if request.user.is_superuser or restaurant_manager.is_manager:
            return True
        else:
            return False


class Is_The_Manager(permissions.BasePermission):
    """ for update and delete a restaurant """

    def has_permission(self, request, view):
        try:
            this_user = RestaurantUser.objects.get(id=request.user.pk)
            restaurant = Restaurant.objects.get(restaurant_manager=request.user.pk)
        except:
            return False

        if request.user.is_superuser or (request.user.pk == restaurant.restaurant_manager_id):
            return True
        else:
            return False


class Is_The_Food_Manager(permissions.BasePermission):
    """ for update and delete a food """

    def has_permission(self, request, view):
        try:
            user_restaurant = Restaurant.objects.get(restaurant_manager=request.user.pk)
            food = Food.objects.get(food_name=request.query_params['food_name'])
            food_restaurant = food.restaurant.pk
        except:
            print('noo')
            return False

        if request.user.is_superuser or (food_restaurant == user_restaurant.pk):
            return True
        else:
            return False


class Is_A_Order_Client(permissions.BasePermission):
    """ for create an order """

    def has_permission(self, request, view):
        try:
            user = RestaurantUser.objects.get(id=request.user.pk)
        except:
            return False

        if request.user.is_superuser or (not user.is_manager):
            return True
        else:
            return False


class Is_The_Order_Client(permissions.BasePermission):
    """ for delete an order """

    def has_permission(self, request, view):
        try:
            user = RestaurantUser.objects.get(id=request.user.pk)
            order = Order.objects.get(order_number=view.kwargs['order_number'])
        except:
            return False

        print(user.pk)
        print(order.client.pk)
        if request.user.is_superuser or (order.client.pk is user.pk):
            return True

        return False


class Is_The_Order_Manager(permissions.BasePermission):
    """ for update(order_received) and retrieve orders """
    def has_permission(self, request, view):
        try:
            user = RestaurantUser.objects.get(id=request.user.pk)
            order = Order.objects.get(order_number=view.kwargs['order_number'])
        except:
            return False

        if request.user.is_superuser:
            return True

        if user.is_manager:
            if order.restaurant.restaurant_manager.pk is user.pk:
                return True
        else:
            if order.client.pk is user.pk:
                return True

        return False


class Is_Super_User(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False


class Is_The_Favorite_Client(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        try:
            user = RestaurantUser.objects.get(id=request.user.pk)
            favorite = FavoriteList.objects.get(client=view.kwargs['client'])
        except:
            print('Is_The_Favorite_Client: no')
            return False

        print(favorite.client.pk)

        if request.user.pk is favorite.client.pk:
            return True

        return False
