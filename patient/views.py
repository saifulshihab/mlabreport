from io import BytesIO
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import patient
from .forms import ProfileUpdateForm
from home.models import lab_report

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
        this_user = patient.objects.get(pemail=user_email)                 
        if request.method == 'POST':                        
            form = ProfileUpdateForm(request.POST, request.FILES, instance=this_user)                            
            if form.is_valid():  
                if (patient.objects.all().filter(phone=form.cleaned_data['phone']) or 
                    patient.objects.all().filter(p_identity=form.cleaned_data['phone'])):
                    alertmsg = "This phone number is not valid!"
                    context = {'profile_update_form': form, 'pa': this_user, 'alert': alertmsg}
                    return render(request, 'patient/profile.html', context)
                else:
                    if this_user.has_pid == True:
                        form.save()                    
                        alertmsg = "Your profile is updated!"                
                        context = {'pa': this_user, 'alert': alertmsg, 'alertcolor': True, 'noform': True, 'has_pid':True}
                        return render(request, 'patient/profile.html', context)
                    else:
                        this_user.p_identity = form.cleaned_data['phone']                
                        this_user.has_pid = True
                        form.save()                    
                        alertmsg = "Your profile is updated!"                
                        context = {'pa': this_user, 'alert': alertmsg, 'alertcolor': True, 'noform': True, 'has_pid':True}
                        return render(request, 'patient/profile.html', context)
        else:                    
            if(this_user.patient_name == "" or 
                this_user.father_name == "" or 
                this_user.mother_name == "" or 
                this_user.phone == ""):
                form = ProfileUpdateForm(instance=this_user) 
                alertmsg = "Please complete your profile information!"
            else:
                form = ProfileUpdateForm(instance=this_user)
            context = {'profile_update_form': form, 'pa': this_user, 'alert': alertmsg}
            return render(request, 'patient/profile.html', context)
    else:
        return redirect('login')

def p_report(request):
    if request.session.has_key('pemail'):        
        this_user = patient.objects.get(pemail=request.session.get('pemail'))                 
        if(this_user.patient_name == "" or 
                this_user.father_name == "" or 
                this_user.mother_name == "" or 
                this_user.phone == ""):
                return redirect('p_profile')
        else:
            has_report = lab_report.objects.filter(p_identity=this_user.pk)
            if has_report:
                context = {'pa': this_user,
                'has_report':has_report
                }            
            else:                
                context = {'pa': this_user,
                'msg':"You have no report right now!"}            
            return render(request, 'patient/report.html', context)                                
    else:
        return redirect('login')

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class view_report(View):    
    def get(self, request, rid, *args, **kwargs):
        context = {'report':lab_report.objects.get(id=rid)}
        lab_report.objects.filter(id=rid).update(seen=True)
        pdf = render_to_pdf('patient/report_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')



