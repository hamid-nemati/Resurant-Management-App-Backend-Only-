from django.urls import path
from rest_framework.routers import DefaultRouter, Route

from manager import views

router = DefaultRouter()
router.register('restaurant-list', views.RestaurantViewset)
router.register('foods', views.FoodViewset)
router.register(r'order', views.OrderViewset)
router.register('favourite', views.FavoriteListViewset)

urlpatterns = [

]

urlpatterns += router.urls
