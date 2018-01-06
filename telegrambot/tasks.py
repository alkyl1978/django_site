# -*- coding: utf-8 -*
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import logging


logger = logging.getLogger('telegrambot')

@shared_task(ignore_result=True)
def bot_update(data, token):
    return
    
    