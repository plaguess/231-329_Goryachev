from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)  # марка
    model = models.CharField(max_length=100)  # модель
    year = models.IntegerField()  # год выпуска
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1)  # объем двигателя
    fuel_type = models.CharField(max_length=50)  # тип топлива
    transmission = models.CharField(max_length=50)  # коробка передач
    color = models.CharField(max_length=50)  # цвет
    mileage = models.IntegerField()  # пробег
    price = models.DecimalField(max_digits=12, decimal_places=2)  # цена
    is_sold = models.BooleanField(default=False)  # продан ли
    added_date = models.DateTimeField(auto_now_add=True)  # дата добавления
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        ordering = ['-added_date']
