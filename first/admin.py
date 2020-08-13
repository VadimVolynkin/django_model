from django.contrib import admin
from . models import Car, Manufacturer



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass