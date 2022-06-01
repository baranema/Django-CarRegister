from django.db import models
from django.core.validators import RegexValidator

CAR_CHOICES = (
    ('Fiat 500','Fiat 500'),
    ('Toyota Corolla','Toyota Corolla'),
    ('Honda CR-V', 'Honda CR-V'),
    ('Nissan Sentra','Nissan Sentra'),
    ('Audi Q4','Audi Q4'),
    ('Honda Civic','Honda Civic'),
    ('BMW X5','BMW X5'),
    ('Volkswagen T-Roc','Volkswagen T-Roc'),
) 

# automobiliams XXX000
# priekaboms XX000
# motociklams 000XX
# mopedams 00XXX
# galingiesiems keturračiams XX00
PLATE_REGEX = r'^([a-zA-Z]{3}[0-9]{3}$|' \
              r'^[0-9]{2}[a-zA-Z]{3}$|' \
              r'^[0-9]{2}[a-zA-Z]{2}$|' \
              r'^[a-zA-Z]{2}[0-9]{3}$)$'

class Car(models.Model):
    #todo add validations for model/plate/firstname/lastname
    carPlateNumber = models.CharField(max_length=6, blank=False, unique=True, validators=[RegexValidator(regex=PLATE_REGEX)])
    carModel = models.CharField(max_length=20, choices=CAR_CHOICES, default='fiat_500') 
    ownerFirstName = models.CharField(max_length=200, blank=False, unique=False)
    ownerLastName = models.CharField(max_length=200, blank=False, unique=False)
    image = models.ImageField(upload_to='media', blank=True, unique=False, editable=False)
    created_at = models.DateTimeField(auto_now=True)