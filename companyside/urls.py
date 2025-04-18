from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('',companyDashboard,name='company_dashboard'),
    path('logout/', logoutCompany, name='company_logout'),

    path('add-job/', add_job, name='add_job'),
]
