# Используем публично доступный образ Python slim как основу
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements.txt и устанавливаем Python зависимости
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем исходный код Django проекта
COPY . /app/

# Создаем директорию для статических файлов
RUN mkdir -p /app/staticfiles

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Применяем миграции при запуске
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"] 