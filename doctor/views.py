from django.shortcuts import render, redirect
from .models import doctor
# Create your views here.
def d_logout(request):
    try:
        del request.session['demail']
    except KeyError:
        pass
    return render(request, 'base/login.html')

def d_dashboard(request):
    if request.session.has_key('demail'):
        user_email = request.session.get('demail')                   
        this_user = doctor.objects.filter(demail=user_email)
        context = {'doctor': this_user}
        return render(request, 'doctor/dashboard.html', context)
    else:
        return redirect('login')