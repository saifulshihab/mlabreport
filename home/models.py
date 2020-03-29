from django.db import models
from patient.models import patient
from django.utils import timezone
# Create your models here.
class organization(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    tel = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class lab_report(models.Model):
    o_name = models.ForeignKey(organization, on_delete=models.CASCADE)
    o_email = models.CharField(max_length=254)
    o_tel = models.CharField(max_length=100)
    o_address = models.CharField(max_length=200)
    p_name = models.CharField(max_length=100)
    p_age = models.CharField(max_length=3)
    p_phone = models.CharField(max_length=11)
    test_1 = models.CharField(max_length=100)
    test1_desc = models.TextField(max_length=500)
    test_2 = models.CharField(max_length=100)
    test2_desc = models.TextField(max_length=500)
    test_3 = models.CharField(max_length=100)
    test3_desc = models.TextField(max_length=500)
    test_4 = models.CharField(max_length=100)
    test4_desc = models.TextField(max_length=500)
    test_5 = models.CharField(max_length=100)
    test5_desc = models.TextField(max_length=500)
    submit_date = models.DateField(default=timezone.now())
    seen = models.BooleanField(default=False)
    p_identity = models.ForeignKey(patient, on_delete=models.CASCADE)

    def get_report(self):
        return f"view_report/{self.id}/"
    def download_report(self):
        return f"DownloadReportasPDF/{self.id}/"
    
    def __str__(self):
        return self.p_identity