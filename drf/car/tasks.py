import os
import tempfile
import glob 
from celery import shared_task
from django.core.files import File
from django.db.models import signals 
from .models import Car 

@shared_task
def get_image(carPlateNumber: str):
    car = Car.objects.get(carPlateNumber=carPlateNumber)  
    images = glob.glob(f"media/{car.carModel.replace(' ', '_')}.*")
    print("this -= ", images, " - car" )
    
    # retrieve locally
    if images:   
        print("hiii")
        Car.objects.filter(carPlateNumber=car.carPlateNumber).update(image=images[len(images)-1]) 

    return None

def car_post_save(sender, instance, **kwargs):  
    if instance.image: 
        # uppercase/lowercase validation needed
        if str(instance.carModel.replace(' ', '_')) not in str(instance.image.url):  
            get_image.delay(instance.carPlateNumber)   
    else:
        get_image.delay(instance.carPlateNumber)  

signals.post_save.connect(car_post_save, sender=Car)