from django.db import models

# Create your models here.

class CompanyRegister(models.Model):   
    email = models.EmailField(null=True, blank=True)
    company_name = models.CharField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.company_name