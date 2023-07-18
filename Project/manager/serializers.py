from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Restaurant, RestaurantUser, FavoriteList, Order, Food
from user_app.serializers import RestaurantUserSerializer


#########################   Restaurant   #########################
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantReadSerializer(serializers.ModelSerializer):
    restaurant_manager = RestaurantUserSerializer()

    class Meta:
        model = Restaurant
        fields = '__all__'


#########################   Food   #########################
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class FoodReadSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = Food
        fields = '__all__'


#########################   Order   #########################
class OrderSerializer(serializers.ModelSerializer):
    # order_price = Food.objects.filter()
    class Meta:
        model = Order
        fields = '__all__'


class OrderReadSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    food = FoodSerializer()
    client = RestaurantUserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


#########################   Favorite List   #########################
class FavoriteListReadSerializer(serializers.ModelSerializer):
    client = RestaurantUserSerializer()
    food = FoodSerializer()

    class Meta:
        model = FavoriteList
        fields = '__all__'


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = '__all__'

#########################   end   #########################
