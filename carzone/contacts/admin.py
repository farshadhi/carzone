from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'car_title', 'car_price', 'first_name', 'last_name', 'city', 'state', 'created_date' )
    list_display_links = ('id', 'first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)


