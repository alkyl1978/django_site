# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from gitweb.views import  repository_listViews

urlpatterns = [
    url(r'^$',repository_listViews.as_view(),name='repository_list'),
]