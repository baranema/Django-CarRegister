from django.db import models

class Car(models.Model):
 carPlate = models.CharField(max_length=120)
 carModel = models.CharField(max_length=120, help_text='Enter your full car model name.')
 ownerfName = models.CharField(max_length=120)
 ownerlName = models.CharField(max_length=120)
 image = models.ImageField(upload_to= 'CarApp/', null=True) 
 
 def __repr__(self):
        return 'Car(%s, %s)' % (self.carPlate, self.carModel, self.ownerfName, self.ownerlName, self.image)

def __str__ (self):
    return self.title 