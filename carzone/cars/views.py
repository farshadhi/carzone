from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cars.choices import inquiry_choices

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct
    city_search = Car.objects.values_list('city', flat=True).distinct
    year_search = Car.objects.values_list('year', flat=True).distinct
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct


    context = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,

    }
    return render(request, 'cars/cars.html', context)

def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)

    context = {
        'single_car': single_car,
        'inquiry_choices': inquiry_choices,
    }
    return render(request, 'cars/car_details.html', context)


def search(request):
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct
    city_search = Car.objects.values_list('city', flat=True).distinct
    year_search = Car.objects.values_list('year', flat=True).distinct
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct
    transmission_search = Car.objects.values_list('transition', flat=True).distinct



    # keyword
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    # model
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    # year
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    # body_style
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    # min_price
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    
        # transmission
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transition__iexact=transmission)



    context = {
    'cars': cars,
    'model_search': model_search,
    'city_search': city_search,
    'year_search': year_search,
    'body_style_search': body_style_search,
    'transmission_search': transmission_search,

    }

    return render(request, 'cars/search.html', context)