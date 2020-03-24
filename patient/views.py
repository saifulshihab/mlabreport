from django.shortcuts import render, redirect
from django.contrib import messages
from .models import patient
from assistant.views import assistantDashboard
from assistant.models import assistant

def patientDashboard(request):
    return render(request, 'patient/dashboard.html')

def p_logout(request):
    try:
        del request.session['pemail']
    except KeyError:
        pass
    return redirect('login')