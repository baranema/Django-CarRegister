from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
    
# Create your models here.
class Car(models.Model):
    carPlateNumber = models.TextField()
    carModel = models.TextField()
    ownerFirstName = models.TextField()
    ownerLastName = models.TextField()
    image = models.ImageField(upload_to=upload_to, null=True)
    created_at = models.DateTimeField(auto_now=True) 