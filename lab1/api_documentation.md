# Документация API автомобильного каталога

## Общая информация

API предоставляет доступ к каталогу автомобилей с возможностью выполнения CRUD-операций (создание, чтение, обновление, удаление), а также поиска, фильтрации и сортировки.

Базовый URL: `/api/cars/`

## Методы API

### 1. Получение списка автомобилей

- **URL:** `/api/cars/`
- **Метод:** `GET`
- **Параметры запроса:**
  - Фильтрация:
    - `brand` - фильтр по марке автомобиля (например, `/api/cars/?brand=Toyota`)
    - `fuel_type` - фильтр по типу топлива (например, `/api/cars/?fuel_type=Бензин`)
    - `transmission` - фильтр по типу коробки передач (например, `/api/cars/?transmission=Автомат`)
    - `is_sold` - фильтр по статусу продажи (например, `/api/cars/?is_sold=true`)
  - Поиск:
    - `search` - поиск по полям: brand, model, color (например, `/api/cars/?search=Camry`)
  - Сортировка:
    - `ordering` - сортировка по полям: price, year, mileage, added_date (например, `/api/cars/?ordering=-price`)
    - Для обратной сортировки используйте `-` перед именем поля
- **Успешный ответ:** Код 200 OK
- **Формат ответа:**
```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  },
  {
    "id": 2,
    "brand": "BMW",
    "model": "X5",
    "year": 2021,
    "engine_volume": "3.0",
    "fuel_type": "Дизель",
    "transmission": "Автомат",
    "color": "Черный",
    "mileage": 15000,
    "price": "4500000.00",
    "is_sold": false,
    "added_date": "2025-05-29T10:15:00Z"
  }
]
```

### 2. Получение информации о конкретном автомобиле

- **URL:** `/api/cars/{id}/`
- **Метод:** `GET`
- **URL-параметры:** `id` - идентификатор автомобиля
- **Успешный ответ:** Код 200 OK
- **Ошибка:** Код 404 Not Found, если автомобиль не найден
- **Формат ответа:**
```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Camry",
  "year": 2022,
  "engine_volume": "2.5",
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Белый",
  "mileage": 10000,
  "price": "2500000.00",
  "is_sold": false,
  "added_date": "2025-05-30T23:45:00Z"
}
```

### 3. Добавление нового автомобиля

- **URL:** `/api/cars/`
- **Метод:** `POST`
- **Заголовки:** `Content-Type: application/json`
- **Тело запроса:**
```json
{
  "brand": "Mercedes-Benz",
  "model": "E-Class",
  "year": 2023,
  "engine_volume": 2.0,
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Серебристый",
  "mileage": 5000,
  "price": 5500000.00,
  "is_sold": false
}
```
- **Успешный ответ:** Код 201 Created
- **Ошибка:** Код 400 Bad Request при неверных данных
- **Формат ответа:**
```json
{
  "id": 3,
  "brand": "Mercedes-Benz",
  "model": "E-Class",
  "year": 2023,
  "engine_volume": "2.0",
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Серебристый",
  "mileage": 5000,
  "price": "5500000.00",
  "is_sold": false,
  "added_date": "2025-05-31T14:30:45Z"
}
```

### 4. Полное обновление информации об автомобиле

- **URL:** `/api/cars/{id}/`
- **Метод:** `PUT`
- **Заголовки:** `Content-Type: application/json`
- **URL-параметры:** `id` - идентификатор автомобиля
- **Тело запроса:**
```json
{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2022,
  "engine_volume": 2.5,
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Красный",
  "mileage": 12000,
  "price": 2450000.00,
  "is_sold": true
}
```
- **Успешный ответ:** Код 200 OK
- **Ошибка:** Код 400 Bad Request при неверных данных или 404 Not Found, если автомобиль не найден
- **Формат ответа:**
```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Camry",
  "year": 2022,
  "engine_volume": "2.5",
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Красный",
  "mileage": 12000,
  "price": "2450000.00",
  "is_sold": true,
  "added_date": "2025-05-30T23:45:00Z"
}
```

### 5. Частичное обновление информации об автомобиле

- **URL:** `/api/cars/{id}/`
- **Метод:** `PATCH`
- **Заголовки:** `Content-Type: application/json`
- **URL-параметры:** `id` - идентификатор автомобиля
- **Тело запроса:**
```json
{
  "price": 4300000.00,
  "mileage": 18000,
  "is_sold": true
}
```
- **Успешный ответ:** Код 200 OK
- **Ошибка:** Код 400 Bad Request при неверных данных или 404 Not Found, если автомобиль не найден
- **Формат ответа:**
```json
{
  "id": 2,
  "brand": "BMW",
  "model": "X5",
  "year": 2021,
  "engine_volume": "3.0",
  "fuel_type": "Дизель",
  "transmission": "Автомат",
  "color": "Черный",
  "mileage": 18000,
  "price": "4300000.00",
  "is_sold": true,
  "added_date": "2025-05-29T10:15:00Z"
}
```

### 6. Удаление автомобиля

- **URL:** `/api/cars/{id}/`
- **Метод:** `DELETE`
- **URL-параметры:** `id` - идентификатор автомобиля
- **Успешный ответ:** Код 204 No Content
- **Ошибка:** Код 404 Not Found, если автомобиль не найден

## Подробные примеры использования

### 1. Примеры получения списка автомобилей (GET)

#### Получение всех автомобилей
```bash
curl -X GET http://localhost:8000/api/cars/
```

**Ответ:**
```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  },
  {
    "id": 2,
    "brand": "BMW",
    "model": "X5",
    "year": 2021,
    "engine_volume": "3.0",
    "fuel_type": "Дизель",
    "transmission": "Автомат",
    "color": "Черный",
    "mileage": 15000,
    "price": "4500000.00",
    "is_sold": false,
    "added_date": "2025-05-29T10:15:00Z"
  },
  {
    "id": 3,
    "brand": "Mercedes-Benz",
    "model": "E-Class",
    "year": 2023,
    "engine_volume": "2.0",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Серебристый",
    "mileage": 5000,
    "price": "5500000.00",
    "is_sold": false,
    "added_date": "2025-05-31T14:30:45Z"
  }
]
```

#### Фильтрация по марке автомобиля
```bash
curl -X GET "http://localhost:8000/api/cars/?brand=Toyota"
```

**Ответ:**
```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  }
]
```

#### Фильтрация по типу топлива
```bash
curl -X GET "http://localhost:8000/api/cars/?fuel_type=Бензин"
```

**Ответ:**
```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  },
  {
    "id": 3,
    "brand": "Mercedes-Benz",
    "model": "E-Class",
    "year": 2023,
    "engine_volume": "2.0",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Серебристый",
    "mileage": 5000,
    "price": "5500000.00",
    "is_sold": false,
    "added_date": "2025-05-31T14:30:45Z"
  }
]
```

#### Поиск автомобилей
```bash
curl -X GET "http://localhost:8000/api/cars/?search=Camry"
```

**Ответ:**
```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  }
]
```

#### Сортировка автомобилей по цене (убывание)
```bash
curl -X GET "http://localhost:8000/api/cars/?ordering=-price"
```

**Ответ:**
```json
[
  {
    "id": 3,
    "brand": "Mercedes-Benz",
    "model": "E-Class",
    "year": 2023,
    "engine_volume": "2.0",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Серебристый",
    "mileage": 5000,
    "price": "5500000.00",
    "is_sold": false,
    "added_date": "2025-05-31T14:30:45Z"
  },
  {
    "id": 2,
    "brand": "BMW",
    "model": "X5",
    "year": 2021,
    "engine_volume": "3.0",
    "fuel_type": "Дизель",
    "transmission": "Автомат",
    "color": "Черный",
    "mileage": 15000,
    "price": "4500000.00",
    "is_sold": false,
    "added_date": "2025-05-29T10:15:00Z"
  },
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  }
]
```

#### Сортировка автомобилей по году выпуска (возрастание)
```bash
curl -X GET "http://localhost:8000/api/cars/?ordering=year"
```

**Ответ:**
```json
[
  {
    "id": 2,
    "brand": "BMW",
    "model": "X5",
    "year": 2021,
    "engine_volume": "3.0",
    "fuel_type": "Дизель",
    "transmission": "Автомат",
    "color": "Черный",
    "mileage": 15000,
    "price": "4500000.00",
    "is_sold": false,
    "added_date": "2025-05-29T10:15:00Z"
  },
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  },
  {
    "id": 3,
    "brand": "Mercedes-Benz",
    "model": "E-Class",
    "year": 2023,
    "engine_volume": "2.0",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Серебристый",
    "mileage": 5000,
    "price": "5500000.00",
    "is_sold": false,
    "added_date": "2025-05-31T14:30:45Z"
  }
]
```

#### Комбинированный запрос (фильтрация + поиск + сортировка)
```bash
curl -X GET "http://localhost:8000/api/cars/?fuel_type=Бензин&search=Авто&ordering=-year"
```

**Ответ:**
```json
[
  {
    "id": 3,
    "brand": "Mercedes-Benz",
    "model": "E-Class",
    "year": 2023,
    "engine_volume": "2.0",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Серебристый",
    "mileage": 5000,
    "price": "5500000.00",
    "is_sold": false,
    "added_date": "2025-05-31T14:30:45Z"
  },
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": "2500000.00",
    "is_sold": false,
    "added_date": "2025-05-30T23:45:00Z"
  }
]
```

### 2. Примеры получения информации о конкретном автомобиле (GET с id)

#### Получение существующего автомобиля
```bash
curl -X GET http://localhost:8000/api/cars/1/
```

**Ответ:**
```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Camry",
  "year": 2022,
  "engine_volume": "2.5",
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Белый",
  "mileage": 10000,
  "price": "2500000.00",
  "is_sold": false,
  "added_date": "2025-05-30T23:45:00Z"
}
```

#### Запрос несуществующего автомобиля
```bash
curl -X GET http://localhost:8000/api/cars/999/
```

**Ответ:**
```json
{
  "detail": "Not found."
}
```

### 3. Примеры добавления нового автомобиля (POST)

#### Добавление автомобиля (все поля)
```bash
curl -X POST http://localhost:8000/api/cars/ \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": 2.5,
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Белый",
    "mileage": 10000,
    "price": 2500000.00,
    "is_sold": false
  }'
```

**Ответ:**
```json
{
  "id": 4,
  "brand": "Toyota",
  "model": "Camry",
  "year": 2022,
  "engine_volume": "2.5",
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Белый",
  "mileage": 10000,
  "price": "2500000.00",
  "is_sold": false,
  "added_date": "2025-05-31T16:45:12Z"
}
```

#### Добавление автомобиля (без необязательных полей)
```bash
curl -X POST http://localhost:8000/api/cars/ \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Audi",
    "model": "A6",
    "year": 2020,
    "engine_volume": 3.0,
    "fuel_type": "Дизель",
    "transmission": "Автомат",
    "color": "Черный",
    "mileage": 25000,
    "price": 3800000.00
  }'
```

**Ответ:**
```json
{
  "id": 5,
  "brand": "Audi",
  "model": "A6",
  "year": 2020,
  "engine_volume": "3.0",
  "fuel_type": "Дизель",
  "transmission": "Автомат",
  "color": "Черный",
  "mileage": 25000,
  "price": "3800000.00",
  "is_sold": false,
  "added_date": "2025-05-31T16:47:32Z"
}
```

#### Попытка добавления с неверными данными
```bash
curl -X POST http://localhost:8000/api/cars/ \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Honda",
    "model": "Accord",
    "year": "не число",
    "engine_volume": 2.4,
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Серый",
    "mileage": 18000,
    "price": 2200000.00
  }'
```

**Ответ:**
```json
{
  "year": [
    "A valid integer is required."
  ]
}
```

### 4. Примеры полного обновления информации об автомобиле (PUT)

#### Полное обновление всех полей
```bash
curl -X PUT http://localhost:8000/api/cars/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": 2.5,
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Красный",
    "mileage": 12000,
    "price": 2450000.00,
    "is_sold": true
  }'
```

**Ответ:**
```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Camry",
  "year": 2022,
  "engine_volume": "2.5",
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Красный",
  "mileage": 12000,
  "price": "2450000.00",
  "is_sold": true,
  "added_date": "2025-05-30T23:45:00Z"
}
```

#### Попытка обновления с отсутствующими обязательными полями
```bash
curl -X PUT http://localhost:8000/api/cars/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Toyota",
    "model": "Camry",
    "color": "Синий"
  }'
```

**Ответ:**
```json
{
  "year": [
    "This field is required."
  ],
  "engine_volume": [
    "This field is required."
  ],
  "fuel_type": [
    "This field is required."
  ],
  "transmission": [
    "This field is required."
  ],
  "mileage": [
    "This field is required."
  ],
  "price": [
    "This field is required."
  ]
}
```

### 5. Примеры частичного обновления информации об автомобиле (PATCH)

#### Обновление нескольких полей
```bash
curl -X PATCH http://localhost:8000/api/cars/2/ \
  -H "Content-Type: application/json" \
    -d '{
        "price": 4300000.00,
        "mileage": 18000,
        "is_sold": true
    }'
```

**Ответ:**
```json
{
  "id": 2,
  "brand": "BMW",
  "model": "X5",
  "year": 2021,
  "engine_volume": "3.0",
  "fuel_type": "Дизель",
  "transmission": "Автомат",
  "color": "Черный",
  "mileage": 18000,
  "price": "4300000.00",
  "is_sold": true,
  "added_date": "2025-05-29T10:15:00Z"
}
```

#### Обновление одного поля
```bash
curl -X PATCH http://localhost:8000/api/cars/3/ \
  -H "Content-Type: application/json" \
  -d '{
    "color": "Золотистый"
  }'
```

**Ответ:**
```json
{
  "id": 3,
  "brand": "Mercedes-Benz",
  "model": "E-Class",
  "year": 2023,
  "engine_volume": "2.0",
  "fuel_type": "Бензин",
  "transmission": "Автомат",
  "color": "Золотистый",
  "mileage": 5000,
  "price": "5500000.00",
  "is_sold": false,
  "added_date": "2025-05-31T14:30:45Z"
}
```

#### Обновление с неверными данными
```bash
curl -X PATCH http://localhost:8000/api/cars/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "year": "не число"
  }'
```

**Ответ:**
```json
{
  "year": [
    "A valid integer is required."
  ]
}
```

### 6. Примеры удаления автомобиля (DELETE)

#### Удаление существующего автомобиля
```bash
curl -X DELETE http://localhost:8000/api/cars/5/
```

**Ответ:**
Пустой ответ с кодом 204 No Content

#### Попытка удаления несуществующего автомобиля
```bash
curl -X DELETE http://localhost:8000/api/cars/999/
```

**Ответ:**
```json
{
  "detail": "Not found."
}
```

## Дополнительные примеры комбинированных запросов

### Фильтрация по нескольким параметрам
```bash
curl -X GET "http://localhost:8000/api/cars/?brand=Toyota&is_sold=true"
```

**Ответ:**
```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Красный",
    "mileage": 12000,
    "price": "2450000.00",
    "is_sold": true,
    "added_date": "2025-05-30T23:45:00Z"
  }
]
```

### Поиск + сортировка
```bash
curl -X GET "http://localhost:8000/api/cars/?search=Бензин&ordering=year"
```

**Ответ:**
```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "engine_volume": "2.5",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Красный",
    "mileage": 12000,
    "price": "2450000.00",
    "is_sold": true,
    "added_date": "2025-05-30T23:45:00Z"
  },
  {
    "id": 3,
    "brand": "Mercedes-Benz",
    "model": "E-Class",
    "year": 2023,
    "engine_volume": "2.0",
    "fuel_type": "Бензин",
    "transmission": "Автомат",
    "color": "Золотистый",
    "mileage": 5000,
    "price": "5500000.00",
    "is_sold": false,
    "added_date": "2025-05-31T14:30:45Z"
  }
]
``` 