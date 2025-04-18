from django.shortcuts import render , redirect
from accounts.models import *
from django.contrib.auth import logout
from .models import *
from django.contrib import messages


# Create your views here.

def companyDashboard(request):
    company_id = request.session.get('company_id')
    if not company_id:
        return redirect('com-login')

    try:
        company = CompanyRegister.objects.get(id=company_id)
        print(f"company : {company}")
        job = Joblist.objects.filter(company=company) 
        print(job)
        context = {'user_logged_in': True, 'company': company, 'jobs': job}
        return render(request, 'comDashboard.html', context)
    except CompanyRegister.DoesNotExist:
        return redirect('com-login')
    

def logoutCompany(request):
    request.session.flush()  # This will delete all session data, effectively logging out the user
    return redirect('com-login')  


def add_job(request):
    company_id = request.session.get('company_id')
    if not company_id:
        return redirect('com-login')  # Redirect to login if no company session

    company = CompanyRegister.objects.get(id=company_id)  # Get the company instance

    if request.method == "POST":
        job_role = request.POST.get('job_role')
        job_type = request.POST.get('job_type')
        location = request.POST.get('location')
        CGPA = request.POST.get('CGPA')
        LPA = request.POST.get('LPA')
        required_skill = request.POST.get('required_skill')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        description = request.POST.get('description')
        application_deadline = request.POST.get('application_deadline')

        job = Joblist(
            company=company,
            job_role=job_role,
            job_type=job_type,
            location=location,
            CGPA=CGPA,
            LPA=LPA,
            required_skill=required_skill,
            qualification=qualification,
            experience=experience,
            description=description,
            application_deadline=application_deadline
        )
        job.save()
        messages.success(request, 'Job posted successfully!')
        return redirect('company_dashboard')
    
    return redirect('company_dashboard')




# def edit_job(request, pk):
#     company_id = request.session.get('company_id')
#     if not company_id:
#         return redirect('company_login')  # Redirect to login if no company session

#     company = CompanyRegister.objects.get(id=company_id)
#     job = Joblist.objects.get(pk=pk, company=company)  # Ensure the job belongs to the logged-in company
    
#     if request.method == 'POST':
#         job.job_role = request.POST.get('job_role')
#         job.job_type = request.POST.get('job_type')
#         job.location = request.POST.get('location')
#         job.CGPA = request.POST.get('CGPA')
#         job.LPA = request.POST.get('LPA')
#         job.required_skill = request.POST.get('required_skill')
#         job.qualification = request.POST.get('qualification')
#         job.experience = request.POST.get('experience')
#         job.description = request.POST.get('description')
#         job.application_deadline = request.POST.get('application_deadline')

#         job.save()
#         messages.success(request, 'Job updated successfully!')
#         return redirect('company_dashboard')
    
#     return render(request, 'company/job_form.html', {'job': job})



