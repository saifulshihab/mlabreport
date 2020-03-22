from django.db import models

class assistant(models.Model):    
    aemail = models.CharField(max_length=254, blank=False)
    password = models.CharField(max_length=50, blank=False)
    assistant_name = models.CharField(max_length=50)    
    phone = models.CharField(max_length=11)    

