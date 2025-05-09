from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('',userDashboard,name='user_dashboard'),
    path('logout/', logoutUser, name='user_logout'),

    path('profile/<str:username>/', profile_view, name='profile_view'),
    path('profile/<str:username>/edit-pers/', edit_personal, name='edit_personal'),
    path('profile/<str:username>/edit-acd/', edit_academic, name='edit_academic'),
    path('profile/<str:username>/upload-resume/', upload_resume, name='upload_resume'),
    path('jobapply/',applyingJob, name='apply_for_job')
]


