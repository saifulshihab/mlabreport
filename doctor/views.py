from django.shortcuts import render, redirect
from .models import doctor
from home.models import lab_report
from .filters import reportFilter
from django.views import View
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


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


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class view_report2(View):    
    def get(self, request, rid, *args, **kwargs):
        context = {'report':lab_report.objects.get(id=rid)}
        lab_report.objects.filter(id=rid).update(seen=True)
        pdf = render_to_pdf('patient/report_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
