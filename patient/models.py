from django.db import models
from PIL import Image
# Create your models here.
class patient(models.Model):
    pemail = models.CharField(max_length=254, blank=False)
    password = models.CharField(max_length=50, blank=False)
    patient_name = models.CharField(max_length=50)
    dp = models.ImageField(default='default.jpg', upload_to='profile_pic')
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    age = models.CharField(max_length=10)
    p_identity = models.CharField(max_length=11)

    def save(self, *args, **kwargs):
        super(patient, self).save(*args, **kwargs)

        img = Image.open(self.dp.path)

        if img.height > 300 or img.width >300:
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.dp.path)