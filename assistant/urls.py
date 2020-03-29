from django.urls import path
from . import views
urlpatterns = [
   path('a_logout', views.a_logout, name="a_logout"),    
   path('a_dashboard', views.a_dashboard, name="a_dashboard"),    
   path('upload_report', views.upload_report, name="upload_report"),    
]