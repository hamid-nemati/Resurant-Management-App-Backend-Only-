from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from url_filter.integrations.drf import DjangoFilterBackend


from .models import RestaurantUser
from .serializers import RestaurantUserSerializer
from .permissions import IsOwnerOfThisProfile


##############################################################################
@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    ser = RestaurantUserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterViewset(viewsets.ModelViewSet):
    queryset = RestaurantUser.objects.all()
    serializer_class = RestaurantUserSerializer
    permission_classes = (AllowAny,)
    #authentication_classes = (TokenAuthentication, )
    http_method_names = ['post', ]


##############################################################################
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, IsOwnerOfThisProfile))
def profile(request):
    try:
        user = RestaurantUser.objects.get(username=request.query_params['username'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = RestaurantUserSerializer(user)
        return Response(ser.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        ser = RestaurantUserSerializer(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserProfileViewset(viewsets.ModelViewSet):
    queryset = RestaurantUser.objects.all()
    serializer_class = RestaurantUserSerializer
    permission_classes = (IsAuthenticated, IsOwnerOfThisProfile)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    http_method_names = ['get', 'put', 'delete']
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'username', 'phone')
    #lookup_field = 'username'

    permission_classes_by_action = {#'create': [Is_A_Order_Client],
                                    'update': [IsOwnerOfThisProfile],
                                    'destroy': [IsOwnerOfThisProfile],
                                    'list': [IsOwnerOfThisProfile],
                                    'retrieve': [IsOwnerOfThisProfile]
                                    }
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]




