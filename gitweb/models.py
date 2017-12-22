# -*- coding: utf-8 -*-
from django.db import models
    
class Repository(models.Model):
    path = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField( blank=True)
    
    class Meta:
        verbose_name = 'Репозитарий'
        verbose_name_plural = 'Репозитарии'

