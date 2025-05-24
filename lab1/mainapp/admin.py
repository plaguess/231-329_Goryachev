from django.contrib import admin
from .models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'fuel_type', 'is_sold']
    list_filter = ['brand', 'fuel_type', 'transmission', 'is_sold', 'year']
    search_fields = ['brand', 'model', 'color']
    ordering = ['-added_date']
