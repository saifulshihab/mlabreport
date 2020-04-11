from django.urls import path
from . import views
urlpatterns = [
   path('d_logout', views.d_logout, name="d_logout"),    
   path('d_dashboard', views.d_dashboard, name="d_dashboard"),       
   path('view_report', views.view_report, name="view_report"),       
   path('view_report2/<int:rid>/', views.view_report2.as_view(), name="view_report2"),
]