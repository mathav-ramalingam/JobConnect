from django.shortcuts import render , redirect
from accounts.models import *
from .models import *
from companyside.models import *
from accounts.models import *
from django.contrib import messages


# Create your views here.
def userDashboard(request):

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user-login')
    
    try:
        user = UserRegister.objects.get(id=user_id)
        joblist = Joblist.objects.all()
        print(joblist)

        context = {'user_logged_in' : True,'user':user, 'job_list' : joblist}
        return render(request, 'userDashboard.html', context)
    
    except UserRegister.DoesNotExist:
        return redirect('user-login')

def logoutUser(request):
    request.session.flush()  # This will delete all session data, effectively logging out the user
    return redirect('user-login')  