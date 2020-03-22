from django.urls import path
from . import views
urlpatterns = [
   path('a_logout', views.a_logout, name="a_logout"),    
]