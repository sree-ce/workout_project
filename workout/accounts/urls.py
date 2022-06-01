from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django import views
from .views import *


urlpatterns = [


    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', UserResgisterView.as_view(), name='customer_registration'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('users/', UserView.as_view(), name='users'),

    path('profile/', profile_view, name='profile'),
    path('profile/<int:pk>/', profile_view_edit, name='profile'),

    path('trainer_registration/', trainer_registration,
         name='trainer_registration'),
    path('Tprofile/', Tprofile_view, name='profile'),
    path('Tprofile/<int:pk>/', trainer_profile_view, name='profile'),


]
