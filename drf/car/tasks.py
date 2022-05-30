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
        car.image = images.pop()   
        car.save()    
    else:   
        # retrieve using google crawler
        directory = tempfile.mkdtemp() 
        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=1,
            storage={'root_dir': directory})

        filters = dict(size='large', type='photo')
        google_crawler.crawl(keyword = car.carModel, filters = filters, max_num = 1, file_idx_offset = 0)
        
        images = os.listdir(directory)

        if images:   
            with open(os.path.join(directory, images.pop()) , "rb") as img: 
                car.image.save(name=f"{car.carModel}.jpg", content=File(img), save=True) 

    return None


def car_post_save(sender, instance, **kwargs):  
    if instance.image: 
        if str(instance.carModel.replace(' ', '_')) not in str(instance.image.url):  
            get_image.delay(instance.carPlateNumber)   
    else:
        get_image.delay(instance.carPlateNumber)  

signals.post_save.connect(car_post_save, sender=Car)