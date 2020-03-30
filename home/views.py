from django.shortcuts import render, redirect
from django.contrib import messages
from assistant.views import a_dashboard
from assistant.models import assistant
from patient.views import patientProfile
from patient.models import patient
from patient.forms import ProfileUpdateForm
from doctor.models import doctor
from doctor.views import d_dashboard
def isLogged(request):
    if request.session.has_key('pemail'):        
        return patientProfile(request)
    elif request.session.has_key('demail'):
        return d_dashboard(request)        
    elif request.session.has_key('aemail'):
        return a_dashboard(request)        
    else:
        return render(request, 'base/login.html')

def login(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']
        if user_select == "doctor":
            uemail = request.POST['email']
            upass = request.POST['password']
            is_login = doctor.objects.filter(demail=uemail, password=upass)
            if is_login:                    
                    request.session['demail'] = uemail
                    return redirect('d_dashboard')
            else:       
                msg = 'failed'
                context = {'msgtype': msg}         
                messages.success(request, "Invalid credential. Try again..")
                return render(request, 'base/login.html', context)
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
                    return redirect('a_dashboard')
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
            uemail = request.POST['email']
            upass = request.POST['password']
            check_multiple = doctor.objects.filter(demail=uemail)
            if check_multiple:
                msg = 'failed'
                context = {'msgtype': msg}
                messages.success(request, "This email is already registered!")
                return render(request, 'base/registration.html', context)
            else:
                acc_create = doctor(demail=uemail, password=upass)
                acc_create.save()                    
                msg = 'success'
                context = {'msgtype': msg}    
                messages.success(request, "doctor account created!")
                return render(request, 'base/registration.html', context)
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
                acc_create.save()                             
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
                acc_create.save()                    
                msg = 'success'
                context = {'msgtype': msg}    
                messages.success(request, "Assistant account created!")
                return render(request, 'base/registration.html', context)         
    else:        
        return render(request, 'base/registration.html')

