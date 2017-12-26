# -*- coding: utf-8 -*
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import logging
from telegram import Update
import json

logger = logging.getLogger('telegrambot')

@shared_task(ignore_result=True)
def bot_update(data=0 ,token=0):
    update = Update.de_json(data, token)
    logger.info(update.message)    
    
    