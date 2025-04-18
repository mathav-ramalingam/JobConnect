from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('users/', LandPage, name='land-page'),
    path('com-auth/', comanyRegister, name='com-register'),
    path('com-login/', companyLogin, name='com-login')
]
