from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Car
from .serializers import CarSerializer

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['brand', 'fuel_type', 'transmission', 'is_sold']
    search_fields = ['brand', 'model', 'color']
    ordering_fields = ['price', 'year', 'mileage', 'added_date']
