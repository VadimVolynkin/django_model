from django.contrib import admin
from . models import SmallAutoFieldClass



@admin.register(SmallAutoFieldClass)
class SmallAutoFieldClassAdmin(admin.ModelAdmin):
    pass