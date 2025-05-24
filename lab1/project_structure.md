## Описание структуры проекта и основных понятий Django

Ниже ключевые файлы и их назначение в ЛР1:

- **manage.py**  
  Скрипт-оболочка для команд: makemigrations, migrate, runserver, createsuperuser.

- **lab1/settings.py**  
  Конфигурация проекта:  
  - INSTALLED_APPS – зарегистрированные приложения  
  - MIDDLEWARE – промежуточные слои  
  - DATABASES – подключение к БД  
  - CORS, локаль, статика и т.д.

- **lab1/urls.py**  
  Маршрутизация:  
  - admin/  
  - API-эндпоинты через DefaultRouter

- **mainapp/models.py**  
  ORM-модель Item с полями разных типов.

- **mainapp/serializers.py**  
  ModelSerializer для преобразования модели ↔ JSON.

- **mainapp/views.py**  
  ItemViewSet на базе ModelViewSet: CRUD + листинг, фильтрация, поиск, сортировка.

- **populate.py**  
  Скрипт Faker для генерации 1000 тестовых записей.

- **README.md**  
  Инструкция по запуску, curl-примеры.

- **requirements.txt**  
  Зависимости: Django, DRF, django-filter, django-cors-headers, psycopg2, faker.

- **db.sqlite3 / PostgreSQL**  
  Локальная БД или контейнер PostgreSQL.

---

**Основные понятия:**

- **Проект vs приложение:** lab1 может содержать несколько app'ов.  
- **Миграции:** makemigrations + migrate — версионирование схемы.  
- **ORM:** БД ↔ Python-классы.  
- **Сериализация:** Python ↔ JSON.  
- **ViewSet + Router:** готовые CRUD-эндпоинты. 
