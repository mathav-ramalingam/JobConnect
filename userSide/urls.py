from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('',userDashboard,name='user_dashboard'),
    path('logout/', logoutUser, name='user_logout'),

]
