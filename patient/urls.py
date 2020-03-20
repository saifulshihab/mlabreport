from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),
]