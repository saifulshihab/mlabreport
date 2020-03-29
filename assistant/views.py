from django.shortcuts import render, redirect
# from home.views import isLogged  
from .models import assistant
from .forms import ReportUploadForm
from home.models import organization, lab_report
from patient.models import patient

def a_logout(request):
    try:
        del request.session['aemail']
    except KeyError:
        pass
    return render(request, 'base/login.html')

def a_dashboard(request):
    if request.session.has_key('aemail'):
        user_email = request.session.get('aemail')                   
        this_user = assistant.objects.filter(aemail=user_email)
        context = {'assis': this_user}
        return render(request, 'assistant/dashboard.html', context)
    else:
        return redirect('login')

def upload_report(request):
    if request.session.has_key('aemail'):
        user_email = request.session.get('aemail')                   
        this_user = assistant.objects.filter(aemail=user_email)
        if request.method == 'POST':
            form = ReportUploadForm(request.POST)
            if form.is_valid():
                org = organization.objects.get(name=form.cleaned_data['o_name'])
                _patient = patient.objects.get(p_identity=form.cleaned_data['p_identity'])
                lab_report.objects.create(**form.cleaned_data, 
                o_email=org.email,
                o_tel=org.tel,
                o_address=org.address,
                p_name=_patient.patient_name,
                p_age=_patient.age,
                p_phone=_patient.phone
                )
                context = {'assis': this_user, 'report_upload_form':form, 'msg':'Report uploaded successfully.'}
                return render(request, 'assistant/upload_report.html', context)        

        else:
            form = ReportUploadForm()
            context = {'assis': this_user, 'report_upload_form':form}
            return render(request, 'assistant/upload_report.html', context)        
    else:
        return redirect('login')