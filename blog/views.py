# -*- coding: utf-8 -*

from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView ,TemplateView

class MainView(TemplateView):
    template_name="blog/app_main.html"

class PostsListView(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 2
    queryset = Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post_detal'

