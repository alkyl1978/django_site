from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
from celery.task import periodic_task
from django.contrib.sessions.models import Session
from datetime import datetime

@periodic_task(ignore_result=True, run_every=crontab(hour=16, minute=33))
def clean_sessions():
    Session.objects.filter(expire_date__lt=datetime.now()).delete()