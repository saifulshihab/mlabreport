from django.shortcuts import render, redirect
from django.contrib import messages
from assistant.views import assistantDashboard
from assistant.models import assistant
from patient.views import patientProfile
from patient.models import patient
from patient.forms import ProfileUpdateForm

def isLogged(request):
    if request.session.has_key('pemail'):        
        return patientProfile(request)
    elif request.session.has_key('demail'):
        pass
    elif request.session.has_key('aemail'):
        return assistantDashboard(request)        
    else:
        return render(request, 'base/login.html')

def login(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']
        if user_select == "doctor":
            pass
        elif user_select == "patient":            
            uemail = request.POST['email']
            upass = request.POST['password']
            is_login = patient.objects.filter(pemail=uemail, password=upass)
            if is_login:                    
                    request.session['pemail'] = uemail
                    return redirect('p_profile')
            else:       
                msg = 'failed'
                context = {'msgtype': msg}         
                messages.success(request, "Invalid credential. Try again..")
                return render(request, 'base/login.html', context)
        else:   
            uemail = request.POST['email']
            upass = request.POST['password']
            is_login = assistant.objects.filter(aemail=uemail, password=upass)
            if is_login:                    
                    request.session['aemail'] = uemail
                    fetch_user = assistant.objects.filter(aemail=uemail)
                    context = {'assis': fetch_user}
                    return render(request, 'assistant/dashboard.html', context)
            else:       
                msg = 'failed'
                context = {'msgtype': msg}         
                messages.success(request, "Invalid credential. Try again..")
                return render(request, 'base/login.html', context)     
    else:   
        return isLogged(request)  

def registration(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']
        if user_select == "doctor":
            pass
        elif user_select == "patient":            
            uemail = request.POST['email']
            upass = request.POST['password']
            check_multiple = patient.objects.filter(pemail=uemail)
            if check_multiple:
                msg = 'failed'
                context = {'msgtype': msg}
                messages.success(request, "This email is already registered!")
                return render(request, 'base/registration.html', context)
            else:
                acc_create = patient(pemail=uemail, password=upass)
                if acc_create.save():
                        messages.success(request, "Error")
                        msg = 'failed'
                        context = {'msgtype': msg}
                        return render(request, 'base/registration.html', context)
                else:            
                    msg = 'success'
                    context = {'msgtype': msg}    
                    messages.success(request, "Patient account created!")
                    return render(request, 'base/registration.html', context)
        else:   
            uemail = request.POST['email']
            upass = request.POST['password']
            check_multiple = assistant.objects.filter(aemail=uemail)
            if check_multiple:
                msg = 'failed'
                context = {'msgtype': msg}
                messages.success(request, "This email is already registered!")
                return render(request, 'base/registration.html', context)
            else:
                acc_create = assistant(aemail=uemail, password=upass)
                if acc_create.save():
                        messages.success(request, "Error")
                        msg = 'failed'
                        context = {'msgtype': msg}
                        return render(request, 'base/registration.html', context)
                else:            
                    msg = 'success'
                    context = {'msgtype': msg}    
                    messages.success(request, "Assistant account created!")
                    return render(request, 'base/registration.html', context)         
    else:        
        return render(request, 'base/registration.html')

