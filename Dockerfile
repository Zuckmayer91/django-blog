# Usamos la versión de Python que tienes instalada
FROM python:3.13-slim

# Evitar que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Mostrar logs en la terminal de Docker Desktop en tiempo real
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalamos dependencias base para Python 3.13 y Django 6
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Instalamos los requerimientos
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamos tu proyecto del blog
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]