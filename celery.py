import os
from celery import Celery

# Устанавливаем переменную окружения с настройками Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bpl.config.settings')

# Создаём экземпляр Celery с именем проекта
app = Celery('bpl')

# Загружаем настройки Celery из settings.py с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем файлы tasks.py во всех установленных приложениях
app.autodiscover_tasks()
