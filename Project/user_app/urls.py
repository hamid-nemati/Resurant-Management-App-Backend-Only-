from django.urls import path ,include
from user_app import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('register-viewset', views.UserRegisterViewset)
router.register('profile-viewset', views.UserProfileViewset)


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

]

urlpatterns += router.urls