from django.shortcuts import render
from django.contrib import messages
from .models import patient
def login(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']
        if user_select == "doctor":
            pass
        elif user_select == "patient":            
            uemail = request.POST['email']
            upass = request.POST['password']
            is_login = patient.objects.filter(email=uemail, password=upass)
            if is_login:                    
                    return render(request, 'patient/dashboard.html')
            else:                
                messages.success(request, "Invalid credential. Try again..")
                return render(request, 'base/login.html')
        else:   
            pass     
    else:        
        return render(request, 'base/login.html')
def registration(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']
        if user_select == "doctor":
            pass
        elif user_select == "patient":            
            uemail = request.POST['email']
            upass = request.POST['password']
            acc_create = patient(email=uemail, password=upass)
            if acc_create.save():
                    messages.success(request, "Error")
                    return render(request, 'base/registration.html')
            else:                
                messages.success(request, "Patient account created!")
                return render(request, 'base/registration.html')
        else:   
            pass         
    else:        
        return render(request, 'base/registration.html')