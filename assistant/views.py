from django.shortcuts import render, redirect
#from patient.views import isLogged cannot import

def assistantDashboard(request):
    return render(request, 'assistant/dashboard.html')

def a_logout(request):
    try:
        del request.session['aemail']
    except KeyError:
        pass
    return render(request, 'base/login.html')