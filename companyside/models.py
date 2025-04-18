from django.db import models
from accounts.models import *

# Create your models here.
#  
class Joblist(models.Model):
    company = models.ForeignKey(CompanyRegister, on_delete=models.CASCADE, null=True, blank=True)
    job_role = models.CharField(max_length=300, null=True, blank=True)
    job_type = models.CharField(max_length=300, null=True, blank=True)  # e.g. Full-time, Part-time, Internship
    location = models.CharField(max_length=1000, null=True, blank=True)
    CGPA = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Usually CGPA is numeric (you can also use DecimalField)
    LPA = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Salary in LPA (Lakhs per Annum) — consider DecimalField too
    required_skill = models.CharField(max_length=5000, null=True, blank=True)  # Skills like "Python, Django, React"
    qualification = models.CharField(max_length=500, null=True, blank=True)  # Degree: B.Tech / BCA etc.
    experience = models.CharField(max_length=100, null=True, blank=True)  # ✨ Added: e.g. "0-2 years" or "Fresher allowed"
    description = models.TextField(default="No description provided", null=True, blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    register_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)  # ✨ Added: allow company to deactivate old jobs without deleting.
    posted_at = models.DateTimeField(auto_now_add=True)  # ✨ Added: so you can show "Posted X days ago"

    def __str__(self):
        company_name = self.company.company_name if self.company else "Unknown Company"
        return f"{self.job_role or 'Job Role'} at {company_name}"
