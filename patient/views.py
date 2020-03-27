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
        fetch_user = patient.objects.get(pemail=user_email)                 
        if request.method == 'POST':                        
            form = ProfileUpdateForm(request.POST, request.FILES, instance=fetch_user)                            
            if form.is_valid():        
                fetch_user.p_identity = form.cleaned_data['phone']                
                form.save()                    
                alertmsg = "Your profile is updated!"                
                context = {'pa': fetch_user, 'alert': alertmsg, 'alertcolor': True, 'noform': True, 'has_pid':True}
                return render(request, 'patient/profile.html', context)
        else:                    
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

    