from django.db import models

# Create your models here.
class doctor(models.Model):
    demail = models.CharField(max_length=254)
    password = models.CharField(max_length=10)    
    doctor_name = models.CharField(max_length=100)