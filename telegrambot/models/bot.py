# -*- coding: utf-8 -*-
from django.db import models

class Bot(models.Model):
    bot = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Bots'