from django.db import models

# Create your models here.
class patient(models.Model):
    pemail = models.CharField(max_length=254, blank=False)
    password = models.CharField(max_length=50, blank=False)
    patient_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    age = models.CharField(max_length=10)