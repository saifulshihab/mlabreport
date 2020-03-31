from django.shortcuts import render, redirect
from .models import doctor
from home.models import lab_report
from .filters import reportFilter
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

def view_report(request):
    if request.session.has_key('demail'):
        user_email = request.session.get('demail')                   
        this_user = doctor.objects.filter(demail=user_email)        
        srcFilter = reportFilter(request.GET, queryset=lab_report.objects.all())
        report = srcFilter.qs
        context = {'doctor': this_user, 'reports': report, 'srcFilter': srcFilter}
        return render(request, 'doctor/viewreport.html', context)
    else:
        return redirect('login')

