from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from celery.task import periodic_task
from django.core.cache import cache


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@periodic_task(ignore_result=True, run_every=crontab(hour=0, minute=0))
def clean_cache():
    cache.clear()


