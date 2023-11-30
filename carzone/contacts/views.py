from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def inquiry(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        car_location = request.POST['car_location']
        car_price = request.POST['car_price']
        team_email = request.POST['team_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, car_id=car_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/' + car_id)
        contact = Contact(first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state,
                          car_title=car_title, car_location=car_location, car_price=car_price, email=email, phone=phone, message=message, user_id=user_id, car_id=car_id)
        
        # sending email
        send_mail(
            'New Car Inquiry',
            'You have a  new inquiry for the car. Please login to your admin pannel for more info.',
            'farshadhayati@gmail.com',
            [team_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your request has been submitted '+car_title+ '. we will get back to you shortly.')
        return redirect('/cars/' + car_id)
    
    # else:
    #     return redirect('inquiry')
