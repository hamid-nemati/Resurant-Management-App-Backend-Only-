from rest_framework import serializers
from django.contrib.auth.models import User
from .models import RestaurantUser


class RestaurantUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = RestaurantUser
        fields = ('username', 'password', 'phone', 'is_manager', 'credit')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
