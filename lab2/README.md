# Лабораторная работа №2: Архитектурные решения

## Описание

Контейнеризация Django API для управления автомобилями с использованием Docker, PostgreSQL и Nginx в качестве обратного прокси.

## Архитектура

```
Client (порт 80) → Nginx → Django (порт 8000) → PostgreSQL (порт 5432)
```

### Компоненты:

1. **Nginx** - обратный прокси-сервер
   - Принимает запросы на порту 80
   - Проксирует `/api` и `/admin` на Django
   - Отдает статические файлы

2. **Django Backend** - API сервер
   - Django REST Framework API
   - Работает на порту 8000 внутри контейнера
   - Подключается к PostgreSQL

3. **PostgreSQL** - база данных
   - Хранит данные об автомобилях
   - Работает на порту 5432

## Запуск проекта

### Предварительные требования:
- Docker
- Docker Compose

### Команды для запуска:

1. **Соберите и запустите все сервисы:**
```bash
docker-compose up --build
```

2. **Запуск в фоновом режиме:**
```bash
docker-compose up -d --build
```

3. **Остановка сервисов:**
```bash
docker-compose down
```

4. **Полная очистка (с удалением данных):**
```bash
docker-compose down -v
```

## Использование API

После запуска API будет доступно по адресу: http://localhost

### Основные endpoint'ы:

- `GET http://localhost/api/cars/` - список всех автомобилей
- `POST http://localhost/api/cars/` - создание автомобиля
- `GET http://localhost/api/cars/{id}/` - получение автомобиля по ID
- `PATCH http://localhost/api/cars/{id}/` - частичное обновление
- `PUT http://localhost/api/cars/{id}/` - полное обновление
- `DELETE http://localhost/api/cars/{id}/` - удаление автомобиля

### Администраторская панель:
- http://localhost/admin (логин: admin, пароль: admin)

## Структура проекта

```
lab2/
├── docker-compose.yaml          # Оркестрация контейнеров
├── backend/                     # Django приложение
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   ├── lab1/                    # Django проект
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   └── mainapp/                 # Django приложение
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── ...
└── nginx/                       # Nginx конфигурация
    ├── Dockerfile
    └── templates/
        └── default.conf.template
```

## Полезные команды

### Просмотр логов:
```bash
docker-compose logs backend
docker-compose logs nginx
docker-compose logs postgres
```

### Выполнение команд в контейнере:
```bash
# Django shell
docker-compose exec backend python manage.py shell

# Создание суперпользователя
docker-compose exec backend python manage.py createsuperuser

# Применение миграций
docker-compose exec backend python manage.py migrate

# Генерация тестовых данных
docker-compose exec backend python manage.py shell -c "from mainapp.gentestdata import gentestdata; gentestdata(100)"
```

### Мониторинг:
```bash
# Статус контейнеров
docker-compose ps

# Использование ресурсов
docker stats
```

## Тестирование

### Проверка работоспособности:

1. **Проверка доступности API:**
```bash
curl http://localhost/api/cars/
```

2. **Создание тестового автомобиля:**
```bash
curl -X POST http://localhost/api/cars/ \
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

3. **Проверка админки:**
Перейдите в браузере по адресу http://localhost/admin

## Особенности реализации

1. **Healthcheck для PostgreSQL** - Django ждет готовности БД
2. **Статические файлы** - обслуживаются через Nginx
3. **Переменные окружения** - настройки БД через env vars
4. **Named volumes** - персистентность данных PostgreSQL
5. **Сети Docker** - изоляция сервисов

## Troubleshooting

### Проблемы с запуском:
1. Проверьте, что порты 80, 8000, 5432 свободны
2. Убедитесь, что Docker запущен
3. Проверьте логи: `docker-compose logs`

### Проблемы с базой данных:
1. Удалите volumes и пересоздайте: `docker-compose down -v && docker-compose up --build`
2. Проверьте healthcheck PostgreSQL: `docker-compose logs postgres` 