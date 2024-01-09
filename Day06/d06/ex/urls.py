from django.contrib import admin
from django.urls import path
from .views import Home,SingUp,SingIn,SingOut,Profile
# from .views import Home,singup

urlpatterns = [
    path('', Home, name='home'),
    path('SingUp/', SingUp, name='SingUp'),
    path('SingIn/', SingIn, name='SingIn'),
    path('SingOut/', SingOut, name='SingOut'),
    path('profile/', Profile, name='profile'),
]