# Пульт охраны
 
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)

## Техническое описание
По предназначено контролировать нахождение сотрудников в красной зоне
и сигнализировать о превышении среднего времени нахождения.

## Системные требования
- [Python 3](https://www.python.org/)
- [Django 1.11](https://www.djangoproject.com/)


##  Установка
Для установки дастоточно:

Cклонировать проект

    $ git clone https://github.com/toshiharu13/django-orm-watching-storage.git

Установить requirements.txt

      $ pip install -r requirements.txt

### Создание файла переменного окружения
В корне проекта создайте и заполние файл .env
В нём будут хранится данные необходимые для подключения к БД postgress
 - DATABASE_URL=postgres://<имя пользователя>:<пароль>@<адрес хоста с БД>:<порт к БД>/<имя базы>
 - DJANGO_SECRET_KEY=<секретный ключ django>
 - TRUSTED_HOSTS=<список даверенных хостов(ALLOWED_HOSTS) через запятую>
 - DEBUG_ON_OFF=<режим дебага true/false>

DEBUG_ON_OFF не является обязательным, если его не указывать, debug примет значение False.

## Запуск

      $ python manage.py runserver 0.0.0.0:8000

