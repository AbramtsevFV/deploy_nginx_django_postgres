## Пример разворачивания Django проекта на VPS

Используется связка docker контейнеров на примере django + nginx + gunicorn + postgresql.

### Настройка docker-compose
 Основные моменты это сервис nginx, есть 2 варианта запуска для локальных тестов и деплой:

- Локальный запуск
```    
        expose:
           - 8080
        ports:
            - "80:8080"
```
- Деплой:
```
        expose:
          - 80
        ports:
          - "80:80"
          - "443:443"
```

Проверить ```volumes ``` в данном примере название директории ``photo_load``, заменить на своё.

### Настройка Dockerfile
    docker/python/Dockerfile
- В данном примере название директории ``photo_load``, заменить на своё.


## Настройка nginx conf
``docker/nginx/158.160.24.98.conf``

Как и в случае с docker-compose есть 2 варианта запуска:

 - Локальный запуск
```    
       listen 8080; 
       server_name localhost;
```
- Деплой:
```
        listen 80; # nginx будет слушать этот порт.
        server_name 158.160.24.98;
```
``server_name`` - имя сайта или сервера

- Так же меняем все директории ```photo_load``` на свои.

## Gunicorn 
В директории ``photo_load`` (директория проекта) создаём файл ``gunicorn.py`` со следующим содержимым:
```python
from multiprocessing import cpu_count
from os import environ

def max_workers():
    return cpu_count()

bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()

env = {
    'DJANGO_SETTINGS_MODULE': 'photo.settings'
}
reload = True
name = 'photo'
```

- меняем ``name`` и ``env`` на свои.

## Сборка
```commandline
docker-compose build
```

## Запуск

```commandline
docker-compose up
```

## Остановка

```commandline
docker-compose down
```

[Использован материал](https://www.haikson.com/programmirovanie/python/django-nginx-gunicorn-postgresql-docker/)