from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.main_photo.url))
    thumbnail.short_description = "photo"

    list_display = ('id', 'thumbnail', 'car_title', 'price', 'created_date', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_filter = ('car_title', 'transition', 'fuel_type')
    search_fields = ('car_title',)
    list_per_page = 50
    list_editable = ('is_featured',)

admin.site.register(Car, CarAdmin)
