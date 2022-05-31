from django.db import models
  
class Car(models.Model):
    #todo add validations for model/plate/firstname/lastname
    carPlateNumber = models.CharField(max_length=6, blank=False, unique=True,)
    carModel = models.CharField(max_length=200, blank=False, unique=False)
    ownerFirstName = models.CharField(max_length=200, blank=False, unique=False)
    ownerLastName = models.CharField(max_length=200, blank=False, unique=False)
    image = models.ImageField(upload_to='media', blank=True, unique=False, editable=False)
    created_at = models.DateTimeField(auto_now=True)