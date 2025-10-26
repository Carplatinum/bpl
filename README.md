Для запуска локально укажите в .env  
DJANGO_ENV=development.

Запускайте сервер и миграции через  
- python manage.py migrate  
- python manage.py runserver

Для продакшен окружения меняйте  
DJANGO_ENV=production.

* Закомментирован Celery для успешого выполнения миграций):  

Модуль config/__init__.py:  

#from bpl.celery import app as celery_app

__all__ = ['celery_app']
