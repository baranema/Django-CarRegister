from django.apps import AppConfig as BaseAppConfig
from django.utils.module_loading import autodiscover_modules

class CarConfig(BaseAppConfig):
    name = 'car'  

    def ready(self):
        autodiscover_modules('tasks')
 
default_app_config = 'car.CarConfig'
