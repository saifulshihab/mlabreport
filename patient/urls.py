from django.urls import path
from . import views
urlpatterns = [    
    path('p_logout', views.p_logout, name="p_logout"),
    path('p_profile', views.patientProfile, name="p_profile"),
    path('p_report', views.p_report, name="p_report"),
    path('view_report/<int:rid>/', views.view_report.as_view(), name="view_report")
]