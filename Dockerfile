FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser /app

RUN apt-get update && apt-get install -y \
    python3-dev \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libonig-dev \
    libxml2-dev \
    nano \
    curl \
    zip \
    unzip \
    git

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER appuser

CMD ["tail", "-f", "/dev/null"]
