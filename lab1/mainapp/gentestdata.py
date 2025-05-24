import random
from decimal import Decimal
import faker
from faker import Faker

from mainapp.models import Car

fake = Faker()

def gentestdata(n=1000):
    # Списки реальных данных для автомобилей
    brands = ['Toyota', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Ford', 'Honda', 
              'Hyundai', 'Kia', 'Nissan', 'Mazda', 'Subaru', 'Skoda', 'Renault', 'Lada']
    
    toyota_models = ['Camry', 'Corolla', 'RAV4', 'Highlander', 'Prius', 'Land Cruiser']
    bmw_models = ['X5', 'X3', 'Serie 3', 'Serie 5', 'X1', 'Serie 7']
    mercedes_models = ['E-Class', 'C-Class', 'S-Class', 'GLE', 'GLC', 'A-Class']
    audi_models = ['A4', 'A6', 'Q5', 'Q7', 'A3', 'Q3']
    volkswagen_models = ['Polo', 'Golf', 'Passat', 'Tiguan', 'Jetta', 'Touareg']
    
    models_by_brand = {
        'Toyota': toyota_models,
        'BMW': bmw_models,
        'Mercedes-Benz': mercedes_models,
        'Audi': audi_models,
        'Volkswagen': volkswagen_models,
    }
    
    fuel_types = ['Бензин', 'Дизель', 'Гибрид', 'Электро', 'Газ']
    transmissions = ['Механическая', 'Автомат', 'Робот', 'Вариатор']
    colors = ['Белый', 'Черный', 'Серый', 'Красный', 'Синий', 'Зеленый', 'Желтый', 'Серебристый']
    
    for _ in range(n):
        brand = random.choice(brands)
        
        # Выбираем модель в зависимости от марки
        if brand in models_by_brand:
            model = random.choice(models_by_brand[brand])
        else:
            model = fake.word().capitalize() + "-" + str(random.randint(100, 999))
        
        year = random.randint(2000, 2024)
        engine_volume = Decimal(random.uniform(1.0, 6.0)).quantize(Decimal('0.1'))
        fuel_type = random.choice(fuel_types)
        transmission = random.choice(transmissions)
        color = random.choice(colors)
        
        # Пробег зависит от года выпуска
        max_mileage = (2024 - year) * 15000
        mileage = random.randint(0, max_mileage) if max_mileage > 0 else 0
        
        # Цена зависит от года, марки и пробега
        base_price = 500000 if brand in ['BMW', 'Mercedes-Benz', 'Audi'] else 300000
        year_factor = 1 + (year - 2000) * 0.05
        mileage_factor = max(0.3, 1 - mileage / 200000)
        price = Decimal(base_price * year_factor * mileage_factor * random.uniform(0.8, 1.2)).quantize(Decimal('0.01'))
        
        is_sold = random.choice([True, False])
        
        Car.objects.create(
            brand=brand,
            model=model,
            year=year,
            engine_volume=engine_volume,
            fuel_type=fuel_type,
            transmission=transmission,
            color=color,
            mileage=mileage,
            price=price,
            is_sold=is_sold
        )
    
    print(f"Создано {n} автомобилей успешно.")
    
if __name__ == '__main__':
    print("Этот скрипт должен быть запущен через Django shell")
    print("python manage.py shell")
    print(">>> from mainapp.gentestdata import *")
    print(">>> gentestdata()") 