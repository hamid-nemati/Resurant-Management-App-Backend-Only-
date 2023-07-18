from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .permissions import Is_A_Manager, Is_The_Manager, Is_The_Food_Manager, Is_The_Favorite_Client
from .permissions import Is_A_Order_Client, Is_The_Order_Client, Is_The_Order_Manager, Is_Super_User

from .models import Restaurant, RestaurantUser, Order, FavoriteList, Food
from .serializers import RestaurantUserSerializer
from .serializers import RestaurantSerializer, RestaurantReadSerializer
from .serializers import OrderSerializer, OrderReadSerializer
from .serializers import FavoriteListSerializer, FavoriteListReadSerializer
from .serializers import FoodSerializer, FoodReadSerializer
from user_app.views import UserProfileViewset

from url_filter.integrations.drf import DjangoFilterBackend


########################   Restaurant    #########################
class RestaurantViewset(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ('restaurant_category', 'restaurant_name')
    ordering_fields = '__all__'
    permission_classes_by_action  = {'create':[Is_A_Manager],
                                     'update': [Is_The_Manager],
                                     'destroy': [Is_The_Manager],
                                     'list':[IsAuthenticated],
                                     'retrieve':[IsAuthenticated]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return RestaurantSerializer
        else:
            return RestaurantReadSerializer


########################   Food    #########################
class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    ordering_fields = '__all__'
    search_fields = ('food_name', 'food_price')
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('food_name', 'available', 'restaurant', 'food_price')
    permission_classes_by_action = {'create': [Is_The_Manager],
                                    'update': [Is_The_Manager],
                                    'destroy': [Is_The_Manager],
                                    'list': [IsAuthenticated],
                                    'retrieve': [IsAuthenticated]
                                    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return FoodSerializer
        else:
            return FoodReadSerializer


########################   Order    #########################
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ('order_number', 'order_received')
    ordering_fields = ('order_number', 'order_received')
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('client', 'restaurant', 'food', 'order_number', 'order_received')
    #lookup_url_kwarg = 'order_number'
    lookup_field = 'order_number'
    permission_classes_by_action = {'create': [Is_A_Order_Client],
                                    'update': [Is_The_Order_Manager],
                                    'destroy': [Is_The_Order_Client],
                                    #'list': [Is_The_Order_Manager],
                                    'retrieve': [Is_The_Order_Manager]
                                    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return OrderSerializer
        else:
            return OrderReadSerializer


    def update(self, request, *args, **kwargs):
        print(kwargs['order_number'])
        obj = super().update(request, *args, **kwargs)
        return obj


########################   Favorite List    #########################
class FavoriteListViewset(viewsets.ModelViewSet):
    queryset = FavoriteList.objects.all()
    http_method_names = ['get',  'post', 'put', 'delete']
    ordering_fields = ('client', 'food')
    search_fields = ('id', 'client', )
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'client', 'food')
    lookup_field = 'id'
    permission_classes_by_action = {'create': [Is_A_Order_Client],
                                    #'update': [Is_The_Favorite_Client],
                                    #'destroy': [Is_The_Favorite_Client],
                                    #'list': [Is_Super_User],
                                    #'retrieve': [Is_The_Favorite_Client]
                                    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return FavoriteListSerializer
        else:
            return FavoriteListReadSerializer


