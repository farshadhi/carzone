from django.db import models
from .choices import state_choices, year_choices, features_choices, door_choices, status_choices, transmission_choices
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

class Car(models.Model):
    car_title = models.CharField(max_length=100)
    state = models.CharField(choices=state_choices)
    city = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    status = models.CharField(choices=status_choices)
    year = models.IntegerField(('year'), choices=year_choices)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    off_price = models.IntegerField()
    description = RichTextField(blank=True)
    main_photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    features = MultiSelectField(choices=features_choices, max_length=200)
    body_style = models.CharField(max_length=100)
    transition = models.CharField(choices=transmission_choices)
    engine = models.CharField(max_length=100, blank=True)
    interior = models.CharField(max_length=100)
    doors = models.CharField(choices=door_choices)
    miles = models.IntegerField()
    milage = models.IntegerField()
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
    

