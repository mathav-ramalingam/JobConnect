from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Joblist)  #model name
class CatagoryAdmin(admin.ModelAdmin):
    list_display =['company','job_role','job_type','location','CGPA','LPA','required_skill','qualification','experience','description','application_deadline','register_count','posted_at']