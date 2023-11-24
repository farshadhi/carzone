from django.shortcuts import render
from .models import Car

def cars(request):
    cars = Car.objects.all().order_by('-created_date')
    context = {
        'cars': cars
    }
    return render(request, 'cars/cars.html', context)