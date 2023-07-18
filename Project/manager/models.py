from django.db import models
from user_app.models import RestaurantUser

    
# class RestaurantManager(models.Model):
#     name = models.CharField(max_length=30)
#     manager_phone = models.CharField(max_length=30)
#     created_date = models.DateTimeField(auto_now=True)
#
#
# class RestaurantClient(models.Model):
#     client_name = models.CharField(max_length=30)
#     client_address = models.CharField(max_length=30)
#     client_phone = models.CharField(max_length=30)
#     client_credit = models.PositiveIntegerField()
#     created_date = models.DateTimeField(auto_now=True)
#     password = models.CharField(max_length=30)


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    restaurant_address = models.CharField(max_length=30)
    restaurant_category = models.CharField(max_length=30,
                                           choices=(('Irani', 'Irani'), ('Italian', 'Italian'), ('FastFood', 'FastFood'),),
                                           default='Irani')
    restaurant_phone_number = models.CharField(max_length=30)
    restaurant_manager = models.OneToOneField(RestaurantUser, on_delete=models.PROTECT)
    restaurant_bank_account_number = models.CharField(max_length=30)
    restaurant_credit = models.PositiveIntegerField()


class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    food_name = models.CharField(max_length=30)
    food_price = models.PositiveIntegerField()
    available = models.BooleanField()


class Order(models.Model):
    client = models.ForeignKey(RestaurantUser, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    how_many = models.PositiveIntegerField(default=1)
    order_number = models.PositiveIntegerField() # orders with same number are sent together
    order_price = models.PositiveIntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    order_received = models.BooleanField()


class FavoriteList(models.Model):
    client = models.ForeignKey(RestaurantUser, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)

