from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


class RestaurantUser(User, models.Model):
    is_manager = models.BooleanField(default=False) # false=client & true=manager
    #phone = PhoneField(blank=True, help_text='Contact phone number')
    phone = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now=True)
    credit = models.PositiveIntegerField()

