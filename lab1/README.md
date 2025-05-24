# Lab1 - Django REST API

Three-tier client-server architecture implementation with Django REST Framework.

## Setup

### Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install django djangorestframework django-filter django-cors-headers psycopg2-binary faker
```

### Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser --no-input --username admin --email admin@example.com
```

## Usage

### Start Server
```bash
python manage.py runserver
```

### Populate Database
```bash
python populate.py
```

### API Endpoints

#### Get Items
```bash
curl -X GET http://127.0.0.1:8000/api/items/
```

#### Create Item
```bash
curl -X POST \
  http://127.0.0.1:8000/api/items/ \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Test Item",
    "description": "Description of test item",
    "quantity": 10,
    "price": "99.99",
    "is_available": true
}'
``` 