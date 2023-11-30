from django.db import models
from datetime import datetime


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    car_location = models.CharField(max_length=100)
    car_price = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email
    