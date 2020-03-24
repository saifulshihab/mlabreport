from django.shortcuts import render, redirect
# from home.views import isLogged  

def assistantDashboard(request):
    return render(request, 'assistant/dashboard.html')

def a_logout(request):
    try:
        del request.session['aemail']
    except KeyError:
        pass
    return render(request, 'base/login.html')