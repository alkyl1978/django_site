# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.bot import Bot
from telegrambot.models import User, Chat, Message, Update

# Register your models here.
admin.site.register(Bot)
admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Update)