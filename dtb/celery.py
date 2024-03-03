
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtb.settings')

app = Celery('dtb')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'brith_date': {
        'task': 'task.tasks.get_brith_date',
        'schedule': crontab(minute=34, hour=14),
    },
}
