import os
import tempfile
import glob 
from celery import shared_task
from django.core.files import File
from django.db.models import signals
from icrawler.builtin import GoogleImageCrawler
from .models import Car 

@shared_task
def get_image(carPlateNumber: str):
    car = Car.objects.get(carPlateNumber=carPlateNumber)  
    images = glob.glob(f"media/{car.carModel.replace(' ', '_')}.*")
    
    # retrieve locally
    if images: 
        car.image = images[len(images)-1]
        car.save()  
    else:   
        # retrieve using google crawler
        directory = tempfile.mkdtemp()
        google_crawler = GoogleImageCrawler(storage={'root_dir': directory})
 
        google_crawler.crawl(keyword = car.carModel, filters = dict(size='large', type='photo'), max_num = 1, file_idx_offset = 0)
        images = os.listdir(directory)

        if images:   
            with open(os.path.join(directory, images[len(images)-1]) , "rb") as img: 
                car.image.save(name=f"{car.carModel}.jpg", content=File(img), save=True) 

    return None

def car_post_save(sender, instance, **kwargs):  
    if instance.image: 
        # uppercase/lowercase validation needed
        if str(instance.carModel.replace(' ', '_')) not in str(instance.image.url):  
            get_image.delay(instance.carPlateNumber)   
    else:
        get_image.delay(instance.carPlateNumber)  

signals.post_save.connect(car_post_save, sender=Car)