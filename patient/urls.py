from django.urls import path
from . import views
urlpatterns = [    
    path('p_logout', views.p_logout, name="p_logout"),
    path('p_profile', views.patientProfile, name="p_profile")
]