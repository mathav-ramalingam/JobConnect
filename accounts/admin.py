from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(CompanyRegister)  #model name
class CatagoryAdmin(admin.ModelAdmin):
    list_display =['email','company_name','location','password']


@admin.register(UserRegister)
class UserCategory(admin.ModelAdmin):
    list_display = ['username','email','phone_number','password']
