from django.shortcuts import render, redirect
from .models import patient
from .forms import ProfileUpdateForm

def p_logout(request):
    try:
        del request.session['pemail']
    except KeyError:
        pass
    return redirect('login')

def patientProfile(request):    
    if request.session.has_key('pemail'):
        alertmsg = ""
        user_email = request.session.get('pemail')                   
        if request.method == 'POST':            
            p = patient.objects.filter(pemail=user_email)                
            form = ProfileUpdateForm(request.POST, request.FILES, instance=p)                            
            if form.is_valid():                                                                
                form.save()
                fetch_user = patient.objects.get(pemail=user_email)                 
                alertmsg = "Your profile is updated!"                
                context = {'pa': fetch_user, 'alert': alertmsg, 'alertcolor': True, 'noform': True}
                return render(request, 'patient/profile.html', context)
        else:        
            fetch_user = patient.objects.get(pemail=user_email)                                
            if(fetch_user.patient_name == "" or 
                fetch_user.father_name == "" or 
                fetch_user.mother_name == "" or 
                fetch_user.phone == ""):
                form = ProfileUpdateForm(instance=fetch_user) 
                alertmsg = "Please complete your profile information!"
            else:
                form = ProfileUpdateForm(instance=fetch_user)
            context = {'profile_update_form': form, 'pa': fetch_user, 'alert': alertmsg}
            return render(request, 'patient/profile.html', context)
    else:
        return redirect('login')

    