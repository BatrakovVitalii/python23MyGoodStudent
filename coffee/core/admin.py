from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    list_display_links = (
        'name', 'email'
    )

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = (
        'title',
    )

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'price')
    list_display_links = (
        'price',
    )

@admin.register(Volume)
class VolumeAdmine(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = (
        'title', 'price'
    )

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = (
        'title', 'price'
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'coffee', 'volume', 'topping', 'get_total_price')
    list_display_links = (
        'profile', 'coffee', 'volume', 'topping', 'get_total_price'
    )