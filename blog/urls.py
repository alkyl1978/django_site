# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views import PostsListView, PostDetailView
from django.views.decorators.cache import cache_page


urlpatterns = [
    url(r'^$', cache_page(60 * 15)(PostsListView.as_view()), name='Postlist'),
    url(r'^(?P<pk>\d+)/$', cache_page(60 * 15)(PostDetailView.as_view()), name='Detallist'),
]
