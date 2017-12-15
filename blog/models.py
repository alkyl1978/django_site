# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class PostManager(models.Manager):
    pass

class Post(models.Model):
    objects= PostManager()
    title = models.CharField(max_length=255) # заголовок поста
    date_create = models.DateTimeField(u'Дата публикации', auto_now_add=True) # дата публикации
    date_update = models.DateTimeField(u'Дата обновления', auto_now_add=True)
    content = models.TextField(max_length=10000) # текст поста
    class Meta:
        pass
    
    def __unicode__(self):
        return self.title
